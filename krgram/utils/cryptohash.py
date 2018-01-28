from _sha256 import sha256
from hashlib import sha1
from pyaes import AES
from krgram import Bytes


class AesKeyIV(object):
	def __init__(self, key, iv):
		self.key = key
		self.iv = iv


class Crypto:
	_IGE_BLOCK_SIZE = 16

	@staticmethod
	def rsa_encrypt(plain, key):
		if isinstance(plain, Bytes):
			plain = plain.to_int(True)
		return Bytes.from_int(pow(plain, key.e, key.n), 256, True)

	@staticmethod
	def aes_ige_encrypt(data, aes_key_iv):
		cipher = AES(aes_key_iv.key)
		iv_1 = aes_key_iv.iv[:Crypto._IGE_BLOCK_SIZE]
		iv_2 = aes_key_iv.iv[Crypto._IGE_BLOCK_SIZE:]

		data = [data[i: i + Crypto._IGE_BLOCK_SIZE] for i in range(0, len(data), Crypto._IGE_BLOCK_SIZE)]
		for i, chunk in enumerate(data):
			iv_1 = data[i] = Bytes(cipher.encrypt(chunk ^ iv_1)) ^ iv_2
			iv_2 = chunk

		return Bytes.flattern(data)

	@staticmethod
	def aes_ige_decrypt(data, aes_key_iv):
		cipher = AES(aes_key_iv.key)
		iv_1 = aes_key_iv.iv[:Crypto._IGE_BLOCK_SIZE]
		iv_2 = aes_key_iv.iv[Crypto._IGE_BLOCK_SIZE:]

		data = [data[i: i + Crypto._IGE_BLOCK_SIZE] for i in range(0, len(data), Crypto._IGE_BLOCK_SIZE)]
		for i, chunk in enumerate(data):
			chunk = Bytes(chunk)
			iv_2 = data[i] = Bytes(cipher.decrypt( chunk ^ iv_2)) ^ iv_1
			iv_1 = chunk

		return Bytes.flattern(data)


class Hash:
	@staticmethod
	def sha1(data):
		if not isinstance(data, Bytes):
			data = Bytes(data)
		hasher = sha1()
		hasher.update(data)
		hash_digest = hasher.digest()
		return Bytes(hash_digest)

	@staticmethod
	def sha256(data):
		hasher = sha256()
		hasher.update(data)
		hash_digest = hasher.digest()
		return Bytes(hash_digest)



