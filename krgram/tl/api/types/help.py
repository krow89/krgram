from krgram.tl.api.types.globals import User
from krgram.tl.core_types.native import TL_string
from krgram.tl.types import *


class appUpdate(TLConstructor):
	ID = 0x8987f311

	def get_structure(self):
		return ("id", TL_int()), ("critical", Bool()), ("url", TL_string()), ("text", TL_string()),


class noAppUpdate(TLConstructor):
	ID = 0xc45a6536


class inviteText(TLConstructor):
	ID = 0x18cb9f78

	def get_structure(self):
		return ("message", TL_string()),


class support(TLConstructor):
	ID = 0x17c6b5f6

	def get_structure(self):
		return ("phone_number", TL_string()), ("user", User()),


class Support(TLConstructedType):
	CONSTRUCTORS_CLASSES = support,


TLRegister.register(Support)


class InviteText(TLConstructedType):
	CONSTRUCTORS_CLASSES = inviteText,


TLRegister.register(InviteText)


class AppUpdate(TLConstructedType):
	CONSTRUCTORS_CLASSES = appUpdate, noAppUpdate,


TLRegister.register(AppUpdate)
