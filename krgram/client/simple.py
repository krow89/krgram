from krgram.client.authorizer import Authorizer
from krgram.client.session import Session
from krgram.mtproto.connection import MTProtoAbridgedConnection
from krgram.mtproto.dcs import DataCenters
from krgram.mtproto.errors import MTProtoFatalError, UnexpectedResponseIdError
from krgram.mtproto.message import EncryptedMsg
from krgram.mtproto.servers_pk import TelegramServersPublicKeys
from krgram.tl.base import TLRegister, TLBaseSerializer
from krgram.tl.stream import TLBytesStream

try:
	import rsa.core
except ImportError:
	print( "rsa module i missing... please install it" )


class MTProtoClient:
	def __init__(self, test_mode=False):
		# TODO: add possibility to change comunicator
		self.connection= None#MTProtoAbridgedConnection()
		self._test_mode= test_mode
		self._curr_dc= DataCenters.get_default().get_datacenter(1)
		self._server_keys= TelegramServersPublicKeys()
		if not self._server_keys.has_keys():
			raise MTProtoFatalError("No valid server fingerprints stored")
		self._comunication_is_open= False
		self._session = None

	def _init_connection(self):
		if self.connection is not None:
			return self.connection
		if self._test_mode:
			if self._curr_dc.test_ip is None:
				raise Exception("Test mode is not supported in this dc")
			host = self._curr_dc.test_ip
		else:
			host = self._curr_dc.production_ip
		conn = MTProtoAbridgedConnection()
		conn.open(host, 443)
		self.connection = conn
		return self.connection


	def connect(self):
		conn = self._init_connection()
		authorizer = Authorizer(self._curr_dc, self._test_mode, conn)
		authorizer.run()
		self._session = Session(authorizer.get_auth_key(), authorizer.get_server_salt())

	def do_req(self, tlreq):
		conn = self._init_connection()
		if self._session is None:
			self.connect()
		session = self._session
		print "session id\n %s\n\nauth_id\n%s" %(session._id, repr(session._auth_key.key_id))
		msg = session.encrypt_message(tlreq)
		conn.send_message(msg)
		resp_msg = EncryptedMsg(0, 0, None)
		conn.read_message_to(resp_msg)
		enc_msg_data_obj = session.decrypt_message( resp_msg.get_message_key(), resp_msg.get_encrypted_message() )
		msg = enc_msg_data_obj.data
		msg_id = msg[:4]
		func_class = TLRegister.get(TLBaseSerializer.deserialize_int32(msg_id))
		if func_class is None:
			# TODO: new error class is needed
			raise UnexpectedResponseIdError(TLBaseSerializer.deserialize_int32(msg_id, False))
		tl_obj = func_class()
		tl_obj.deserialize_from( TLBytesStream(msg) )
		return tl_obj

	def _close_comunication(self):
		self.connection.close()
		self._comunication_is_open= False

