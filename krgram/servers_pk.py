import rsa

from krgram.tl.auth import TL_int_as_string
from krgram.tl.types import TL_long
from krgram.utils.cryptohash import Hash

_know_servers_pub_keys = (
	'''-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAwVACPi9w23mF3tBkdZz+zwrzKOaaQdr01vAbU4E1pvkfj4sqDsm6
lyDONS789sVoD/xCS9Y0hkkC3gtL1tSfTlgCMOOul9lcixlEKzwKENj1Yz/s7daS
an9tqw3bfUV/nqgbhGX81v/+7RFAEd+RwFnK7a+XYl9sluzHRyVVaTTveB2GazTw
Efzk2DWgkBluml8OREmvfraX3bkHZJTKX4EQSjBbbdJ2ZXIsRrYOXfaA+xayEGB+
8hdlLmAjbCVfaigxX0CDqWeR1yFL9kwd9P0NsZRPsmoqVwMbMu7mStFai6aIhc3n
Slv8kg9qv1m6XHVQY3PnEw+QQtqSIXklHwIDAQAB
-----END RSA PUBLIC KEY-----''',

	'''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAruw2yP/BCcsJliRoW5eB
VBVle9dtjJw+OYED160Wybum9SXtBBLXriwt4rROd9csv0t0OHCaTmRqBcQ0J8fx
hN6/cpR1GWgOZRUAiQxoMnlt0R93LCX/j1dnVa/gVbCjdSxpbrfY2g2L4frzjJvd
l84Kd9ORYjDEAyFnEA7dD556OptgLQQ2e2iVNq8NZLYTzLp5YpOdO1doK+ttrltg
gTCy5SrKeLoCPPbOgGsdxJxyz5KKcZnSLj16yE5HvJQn0CNpRdENvRUXe6tBP78O
39oJ8BTHp9oIjd6XWXAsp2CvK45Ol8wFXGF710w9lwCGNbmNxNYhtIkdqfsEcwR5
JwIDAQAB
-----END PUBLIC KEY-----''',

	'''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs/ditzm+mPND6xkhzwFI
z6J/968CtkcSE/7Z2qAJiXbmZ3UDJPGrzqTDHkO30R8VeRM/Kz2f4nR05GIFiITl
4bEjvpy7xqRDspJcCFIOcyXm8abVDhF+th6knSU0yLtNKuQVP6voMrnt9MV1X92L
GZQLgdHZbPQz0Z5qIpaKhdyA8DEvWWvSUwwc+yi1/gGaybwlzZwqXYoPOhwMebzK
Uk0xW14htcJrRrq+PXXQbRzTMynseCoPIoke0dtCodbA3qQxQovE16q9zz4Otv2k
4j63cz53J+mhkVWAeWxVGI0lltJmWtEYK6er8VqqWot3nqmWMXogrgRLggv/Nbbo
oQIDAQAB
-----END PUBLIC KEY-----''',

	'''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvmpxVY7ld/8DAjz6F6q0
5shjg8/4p6047bn6/m8yPy1RBsvIyvuDuGnP/RzPEhzXQ9UJ5Ynmh2XJZgHoE9xb
nfxL5BXHplJhMtADXKM9bWB11PU1Eioc3+AXBB8QiNFBn2XI5UkO5hPhbb9mJpjA
9Uhw8EdfqJP8QetVsI/xrCEbwEXe0xvifRLJbY08/Gp66KpQvy7g8w7VB8wlgePe
xW3pT13Ap6vuC+mQuJPyiHvSxjEKHgqePji9NP3tJUFQjcECqcm0yV7/2d0t/pbC
m+ZH1sadZspQCEPPrtbkQBlvHb4OLiIWPGHKSMeRFvp3IWcmdJqXahxLCUS1Eh6M
AQIDAQAB
-----END PUBLIC KEY-----'''
)


class PublicKey:
	def __init__(self, n, e):
		self.n = n
		self.e = e
		try:
			self.fingerprint = PublicKey._compute_fingerprint(n, e)
		except Exception as e:
			print e
			raise e

	@staticmethod
	def _compute_fingerprint(n, e):
		tln = TL_int_as_string(n, size=(n.bit_length() + 7) // 8)
		tle = TL_int_as_string(e, size=(e.bit_length() + 7) // 8)
		hashed_data = Hash.sha1(tln.serialize() + tle.serialize())
		l = TL_long(hashed_data[-8:])
		return l.get()


class TelegramServersPublicKeys(object):
	_instance = None

	def __new__(cls, *args, **kwargs):
		if TelegramServersPublicKeys._instance is None:
			pkeys = _rsa_keys_to_keys(_know_servers_pub_keys)
			obj = object.__new__(cls)
			obj._pkeys = pkeys
			cls._instance = obj
		return TelegramServersPublicKeys._instance

	def get_key_by_fingerprint(self, fingerprint):
		for pk in self._pkeys:
			if pk.fingerprint == fingerprint:
				return pk

	def get_keys(self):
		return self._pkeys[:]

	def has_keys(self):
		return len(self._pkeys) > 0

	def __getitem__(self, item):
		for k in self._instance._pkeys:
			if k.fingerprint == item:
				return k
		return None


def _rsa_keys_to_keys(pkeys):
	ret = []
	for i in pkeys:

		try:
			rsa_pk = rsa.PublicKey.load_pkcs1(i)
			ret.append(PublicKey(rsa_pk.n, rsa_pk.e))
			continue
		except Exception as e:
			pass
		try:
			rsa_pk = rsa.PublicKey.load_pkcs1_openssl_der(i)
			ret.append(PublicKey(rsa_pk.n, rsa_pk.e))
			continue
		except Exception as e:
			pass
		try:
			rsa_pk = rsa.PublicKey.load_pkcs1_openssl_pem(i)
			ret.append(PublicKey(rsa_pk.n, rsa_pk.e))
			continue
		except Exception as e:
			pass

	return ret
