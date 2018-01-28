from krgram.tl.types import *


class checkPhone(TLFunction):
	ID = 0x6fe51dfb

	def get_structure(self):
		return ("phone_number", TL_string()), 

TLRegister.register(checkPhone)


class sendCode(TLFunction):
	ID = 0x768d5f4d

	def get_structure(self):
		return ("phone_number", TL_string()), ("sms_type", TL_int()), ("api_id", TL_int()), ("api_hash", TL_string()), ("lang_code", TL_string()), 

TLRegister.register(sendCode)


class sendCall(TLFunction):
	ID = 0x3c51564

	def get_structure(self):
		return ("phone_number", TL_string()), ("phone_code_hash", TL_string()), 

TLRegister.register(sendCall)


class signUp(TLFunction):
	ID = 0x1b067634

	def get_structure(self):
		return ("phone_number", TL_string()), ("phone_code_hash", TL_string()), ("phone_code", TL_string()), ("first_name", TL_string()), ("last_name", TL_string()), 

TLRegister.register(signUp)


class signIn(TLFunction):
	ID = 0xbcd51581

	def get_structure(self):
		return ("phone_number", TL_string()), ("phone_code_hash", TL_string()), ("phone_code", TL_string()), 

TLRegister.register(signIn)


class logOut(TLFunction):
	ID = 0x5717da40

TLRegister.register(logOut)


class resetAuthorizations(TLFunction):
	ID = 0x9fab0d1a

TLRegister.register(resetAuthorizations)


class sendInvites(TLFunction):
	ID = 0x771c1d97

	def get_structure(self):
		return ("phone_numbers", Vector()), ("message", TL_string()), 

TLRegister.register(sendInvites)


class exportAuthorization(TLFunction):
	ID = 0xe5bfffcd

	def get_structure(self):
		return ("dc_id", TL_int()), 

TLRegister.register(exportAuthorization)


class importAuthorization(TLFunction):
	ID = 0xe3ef9613

	def get_structure(self):
		return ("id", TL_int()), ("bytes", TL_bytes()), 

TLRegister.register(importAuthorization)


class bindTempAuthKey(TLFunction):
	ID = 0xcdd42a05

	def get_structure(self):
		return ("perm_auth_key_id", TL_long()), ("nonce", TL_long()), ("expires_at", TL_int()), ("encrypted_message", TL_bytes()), 

TLRegister.register(bindTempAuthKey)


class sendSms(TLFunction):
	ID = 0xda9f3e8

	def get_structure(self):
		return ("phone_number", TL_string()), ("phone_code_hash", TL_string()), 

TLRegister.register(sendSms)

