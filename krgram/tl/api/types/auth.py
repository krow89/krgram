from krgram.tl.api.types.globals import User
from krgram.tl.types import *


class checkedPhone(TLConstructor):
	ID = 0xe300cc3b

	def get_structure(self):
		return ("phone_registered", Bool()), ("phone_invited", Bool()),


class sentCode(TLConstructor):
	ID = 0xefed51d9

	def get_structure(self):
		return ("phone_registered", Bool()), ("phone_code_hash", TL_string()), ("send_call_timeout", TL_int()), (
			"is_password", Bool()),


class sentAppCode(TLConstructor):
	ID = 0xe325edcf

	def get_structure(self):
		return ("phone_registered", Bool()), ("phone_code_hash", TL_string()), ("send_call_timeout", TL_int()), (
			"is_password", Bool()),


class authorization(TLConstructor):
	ID = 0xf6b673a4

	def get_structure(self):
		return ("expires", TL_int()), ("user", User()),


class exportedAuthorization(TLConstructor):
	ID = 0xdf969c2d

	def get_structure(self):
		return ("id", TL_int()), ("bytes", TL_bytes()),


class CheckedPhone(TLConstructedType):
	CONSTRUCTORS_CLASSES = checkedPhone,


TLRegister.register(CheckedPhone)


class SentCode(TLConstructedType):
	CONSTRUCTORS_CLASSES = sentCode, sentAppCode,


TLRegister.register(SentCode)


class Authorization(TLConstructedType):
	CONSTRUCTORS_CLASSES = authorization,


TLRegister.register(Authorization)


class ExportedAuthorization(TLConstructedType):
	CONSTRUCTORS_CLASSES = exportedAuthorization,


TLRegister.register(ExportedAuthorization)
