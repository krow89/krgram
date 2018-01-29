import os
from time import time

import krgram.tl.protocol
from krgram import Bytes
from krgram.client.crypto import TLEncryptor
from krgram.client.errors import SecurityError
from krgram.mtproto.connection import MTProtoAbridgedConnection
from krgram.mtproto.dcs import DataCenters
from krgram.mtproto.errors import UnexpectedResponseError
from krgram.mtproto.message import PlainMsg
from krgram.mtproto.msg_extra import MsgId
from krgram.servers_pk import TelegramServersPublicKeys
from krgram.tl.base import *
from krgram.tl.core_types.native_extends import TL_int128, TL_int256
from krgram.tl.stream import TLBytesStream
from krgram.utils.cryptohash import Hash, Crypto
from krgram.utils.math import factorize


class AuthKey:
	def __init__(self, data):
		self.data = data
		self.key_id = None
		self._calculate_id()

	def get_id(self):
		return self.key_id

	def _calculate_id(self):
		if self.data is not None:
			self.key_id = Hash.sha1(self.data)[-8:]
		else:
			self.key_id = Bytes('\x00'*8)


class Authorizer:
	_NULL_AUTH_KEY = AuthKey(None)

	def __init__(self, dc, test_mode=False, connection=None ):
		self.dc = dc
		self.test_mode = test_mode
		self._connection = connection
		self._server_salt = None
		self._server_time_diff = -1
		self._auth_key = None

	def get_auth_key(self):
		return self._auth_key

	def get_server_salt(self):
		return self._server_salt

	def get_server_time_diff(self):
		return self._server_time_diff

	def run(self):
		conn = self._connection
		autoclose = False
		if conn is None:
			conn = self._init_connection(self.dc, self.test_mode)
			autoclose = True
		raw_nonce = os.urandom(16)
		obj = krgram.tl.protocol.req_pq(nonce=raw_nonce)
		nonce = obj.nonce#["nonce"]
		resp_tl_obj = self._send_plain_req(conn, obj)
		#resp_tl_obj = msg.get_content()
		if resp_tl_obj.ID != krgram.tl.protocol.resPQ.ID:
			raise UnexpectedResponseError("Expected a resPQ object")
		if resp_tl_obj.nonce != obj.nonce:
			raise SecurityError("nonce != (server)nonce")
		server_nonce, pub_srvs_fingerprints = resp_tl_obj.server_nonce, resp_tl_obj.server_public_key_fingerprints

		# check fingerprint
		curr_key = None
		for f in pub_srvs_fingerprints:
			cpk = TelegramServersPublicKeys().get_key_by_fingerprint(f)
			if cpk is not None:
				curr_key = cpk
				break

		# compute p and q
		pq = resp_tl_obj.pq#["pq"]
		p, q = factorize(pq)
		p, q = (p, q) if p < q else (q, p)
		new_nonce = os.urandom(32)
		obj = krgram.tl.protocol.p_q_inner_data(p=p,
												q=q,
												pq=pq,
												server_nonce=server_nonce,
												nonce=nonce,
												new_nonce=new_nonce)
		pq_inner_data_serialized = obj.serialize()
		data_with_hash = Hash.sha1(pq_inner_data_serialized) + pq_inner_data_serialized
		if len(data_with_hash) < 255:
			data_with_hash += Bytes('\0' * (255 - len(data_with_hash)))

		# encrypt with rsa and send data
		enc_data = Crypto.rsa_encrypt(data_with_hash, curr_key)
		obj = krgram.tl.protocol.req_DH_params(nonce=nonce,
											   p=p,
											   q=q,
											   server_nonce=server_nonce,
											   public_key_fingerprint=curr_key.fingerprint,
											   encrypted_data=enc_data)
		resp_tl_obj = self._send_plain_req(conn, obj)
		#resp_tl_obj = msg.get_content()
		if resp_tl_obj.nonce != nonce or resp_tl_obj.server_nonce != server_nonce:
			raise SecurityError()
		server_nonce_raw = TL_int128(server_nonce).serialize()
		new_nonce_raw = TL_int256(new_nonce).serialize()
		server_salt = new_nonce_raw[:8] ^ server_nonce_raw[:8]
		server_dh = TLEncryptor.decrypt_server_dh(new_nonce_raw, server_nonce_raw, resp_tl_obj.encrypted_answer)
		# TODO: check hash
		# answer_hash = server_dh.data_hash
		answer = server_dh.data
		id_answer_class = Bytes(answer[:4]).to_int(False, False)
		register_class = TLRegister.get_func_type(id_answer_class)
		if register_class is None or register_class.ID != krgram.tl.protocol.server_DH_inner_data.ID:
			raise UnexpectedResponseError("Unexpected response type from server")
		tlstream = TLBytesStream(answer)
		#tlstream.write(answer[4:])
		resp_tl_obj = krgram.tl.protocol.server_DH_inner_data().deserialize_from(tlstream)
		g_a = resp_tl_obj.g_a
		server_time_diff = resp_tl_obj.server_time - int(time())
		b_raw = os.urandom(256)
		b = Bytes(b_raw).to_int()
		g = resp_tl_obj.g
		dh_prime = resp_tl_obj.dh_prime
		g_b = pow(g, b, dh_prime)
		retry_id = 0
		data = krgram.tl.protocol.client_DH_inner_data(nonce=nonce,
													   server_nonce=server_nonce,
													   retry_id=retry_id,
													   g_b=g_b).serialize()
		enc_data = TLEncryptor.encrypt_client_dh(data, server_dh.aes_key_iv)
		obj = krgram.tl.protocol.set_client_DH_params(nonce=nonce,
													  server_nonce=server_nonce,
													  encrypted_data=enc_data)
		resp_tl_obj = self._send_plain_req(conn, obj)
		#resp_tl_obj = msg.get_content()
		if resp_tl_obj.ID != krgram.tl.protocol.dh_gen_ok.ID:
			raise Exception("DH generation not succesfull")
		auth_key = pow(g_a, b, dh_prime)
		auth_key = Bytes.from_int(auth_key, 256)
		if autoclose:
			conn.close()
		auth_key = AuthKey(auth_key)
		self._server_salt = TLBasicTypeSerializer.deserialize_long(server_salt)
		self._auth_key = auth_key
		self._server_time_diff = server_time_diff

	def _init_connection(self, dc, test_mode):
		if dc is None:
			dc = DataCenters.get_default().get_datacenter(1)
		conn = MTProtoAbridgedConnection()
		ip = dc.production_ip if not test_mode else dc.test_ip
		try:
			conn.open( ip, 443 )
			return conn
		except:
			raise Exception("Cannot open a connection on %s:%d" %(ip, 443))

	def _send_plain_req(self, conn, req):
		if not isinstance(req, TLFunction):
			raise TypeError("obj must be an TLFunction instance")
		msg_id = MsgId()()
		raw_msg = PlainMsg(msg_id, req)
		conn.send_message( raw_msg )
		resp_msg = PlainMsg(0, None)
		conn.read_message_to(resp_msg)
		return resp_msg.content
