from krgram.tl.api.types.globals import InputNotifyPeer, InputPeerNotifySettings, InputPeer, ReportReason
from krgram.tl.core_types.native import TL_string
from krgram.tl.types import *


class registerDevice(TLFunction):
	ID = 0x446c712c

	def get_structure(self):
		return ("token_type", TL_int()), ("token", TL_string()), ("device_model", TL_string()), (
		"system_version", TL_string()), ("app_version", TL_string()), ("app_sandbox", Bool()), (
			   "lang_code", TL_string()),


TLRegister.register(registerDevice)


class unregisterDevice(TLFunction):
	ID = 0x65c55b40

	def get_structure(self):
		return ("token_type", TL_int()), ("token", TL_string()),


TLRegister.register(unregisterDevice)


class updateNotifySettings(TLFunction):
	ID = 0x84be5b93

	def get_structure(self):
		return ("peer", InputNotifyPeer()), ("settings", InputPeerNotifySettings()),


TLRegister.register(updateNotifySettings)


class getNotifySettings(TLFunction):
	ID = 0x12b3ad31

	def get_structure(self):
		return ("peer", InputNotifyPeer()),


TLRegister.register(getNotifySettings)


class resetNotifySettings(TLFunction):
	ID = 0xdb7e1747


TLRegister.register(resetNotifySettings)


class updateProfile(TLFunction):
	ID = 0xf0888d68

	def get_structure(self):
		return ("first_name", TL_string()), ("last_name", TL_string()),


TLRegister.register(updateProfile)


class updateStatus(TLFunction):
	ID = 0x6628562c

	def get_structure(self):
		return ("offline", Bool()),


TLRegister.register(updateStatus)


class getWallPapers(TLFunction):
	ID = 0xc04cfac2


TLRegister.register(getWallPapers)


class reportPeer(TLFunction):
	ID = 0xae189d5f

	def get_structure(self):
		return ("peer", InputPeer()), ("reason", ReportReason()),


TLRegister.register(reportPeer)


class checkUsername(TLFunction):
	ID = 0x2714d86c

	def get_structure(self):
		return ("username", TL_string()),


TLRegister.register(checkUsername)


class updateUsername(TLFunction):
	ID = 0x3e0bdd7c

	def get_structure(self):
		return ("username", TL_string()),


TLRegister.register(updateUsername)
