import os

from krgram import Bytes
from krgram.utils.cryptohash import Hash, Crypto, AesKeyIV


class DHServerData:
	def __init__(self, data, hash_data, aes_key_iv):
		self.data = data
		self.data_hash = hash_data
		self.aes_key_iv = aes_key_iv


class TLEncryptor:
	@classmethod
	def _message_encryption(cls, auth_key, msg_key, data, for_encrypt=True):
		x = 0 if for_encrypt else 8
		sha256_a = Hash.sha256(msg_key + auth_key[x: x + 36])
		sha256_b = Hash.sha256(auth_key[x + 40: x + 76] + msg_key)
		aes_key = sha256_a[:8] + sha256_b[8:24] + sha256_a[24:32]
		aes_iv = sha256_b[:8] + sha256_a[8:24] + sha256_b[24:32]
		if for_encrypt:
			return Crypto.aes_ige_encrypt(data, AesKeyIV(aes_key, aes_iv))
		else:
			return Crypto.aes_ige_decrypt(data, AesKeyIV(aes_key, aes_iv))

	@classmethod
	def encrypt_message(cls, auth_key, msg_key, data):
		return cls._message_encryption(auth_key, msg_key, data, True)

	@classmethod
	def decrypt_message(cls, auth_key, msg_key, data):
		return cls._message_encryption(auth_key, msg_key, data, False)

	@staticmethod
	def decrypt_server_dh(new_nonce, server_nonce, encrypted_answer):
		tmp_aes_key = (
			Hash.sha1(new_nonce + server_nonce) + Hash.sha1(server_nonce + new_nonce)[:12]
		)
		tmp_aes_iv = (Hash.sha1(server_nonce + new_nonce)[12:]
					  + Hash.sha1(new_nonce + new_nonce) + new_nonce[:4])
		aes_key_iv = AesKeyIV(tmp_aes_key, tmp_aes_iv)

		answer_with_hash = Crypto.aes_ige_decrypt(encrypted_answer, aes_key_iv)
		data_hash = answer_with_hash[:20]
		data = answer_with_hash[20:]
		return DHServerData(data, data_hash, aes_key_iv)

	@staticmethod
	def encrypt_client_dh(data, server_dh_aes_key_iv):
		data_with_hash = Hash.sha1(data) + data
		if len(data_with_hash) % 16 != 0:
			pad = 16 - len(data_with_hash) % 16
			data_with_hash += Bytes(os.urandom(pad))
		return Crypto.aes_ige_encrypt(data_with_hash, server_dh_aes_key_iv)
