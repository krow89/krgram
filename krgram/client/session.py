from krgram.client.authorizer import AuthKey
from krgram.client.crypto import TLEncryptor
from krgram.mtproto.message import EncryptedMsgData, EncryptedMsg
from krgram.mtproto.msg_extra import SessionId, MsgSeqNo, MsgId
from krgram.utils.cryptohash import Hash


class Session:
	def __init__(self, auth_key, server_salt):
		assert isinstance(auth_key, AuthKey)
		self._auth_key = auth_key
		self._id = SessionId.create()
		self._msg_seq_no = MsgSeqNo()
		self._msg_ids = MsgId()
		self._last_server_salt = server_salt

	def get_id(self):
		return self._id

	def get_auth_key(self):
		return self._auth_key

	def get_current_msg_seq_no(self):
		return self._msg_seq_no

	def get_last_server_salt(self):
		return self._last_server_salt

	def encrypt_message(self, tlreq):
		msg_serialized = tlreq.serialize()
		data = EncryptedMsgData(self._last_server_salt,
								self._id(),
								self._msg_ids(),
								self._msg_seq_no(),
								msg_serialized).serialize()
		auth_key_data = self._auth_key.data
		auth_key_id = self._auth_key.get_id()
		# calculate msg_key
		msg_key = Hash.sha256( auth_key_data[88:88+32] + data )[8:24]
		# ... and encrypt
		enc_data = TLEncryptor.encrypt_message(auth_key_data, msg_key, data)
		return EncryptedMsg(auth_key_id, msg_key, enc_data)

	def decrypt_message(self, msg_key, encrypted_msg):
		auth_key = self._auth_key
		decrypted_raw = TLEncryptor.decrypt_message(auth_key.key, msg_key, encrypted_msg)
		enc_msg = EncryptedMsgData(None, None, None, None, None).deserialize(decrypted_raw)
		return enc_msg

