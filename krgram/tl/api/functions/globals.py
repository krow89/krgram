from krgram.tl.types import *


class invokeAfterMsg(TLFunction):
	ID = 0xcb9f372d

	def get_structure(self):
		return ("msg_id", TL_long()), ("query", TL_Ref()),


TLRegister.register(invokeAfterMsg)


class invokeAfterMsgs(TLFunction):
	ID = 0x3dc4b4f0

	def get_structure(self):
		return ("msg_ids", Vector()), ("query", TL_Ref()),


TLRegister.register(invokeAfterMsgs)


class initConnection(TLFunction):
	ID = 0x69796de9

	def get_structure(self):
		return ("api_id", TL_int()), ("device_model", TL_string()), ("system_version", TL_string()),\
			   ("app_version", TL_string()), ("lang_code", TL_string()), ("query", TL_Ref()),


TLRegister.register(initConnection)


class invokeWithLayer18(TLFunction):
	ID = 0x1c900537

	def get_structure(self):
		return ("query", TL_Ref()),


TLRegister.register(invokeWithLayer18)
