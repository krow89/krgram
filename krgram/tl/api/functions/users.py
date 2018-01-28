from krgram.tl.api.types.globals import InputUser
from krgram.tl.types import *


class getUsers(TLFunction):
	ID = 0xd91a548

	def get_structure(self):
		return ("id", Vector()),


TLRegister.register(getUsers)


class getFullUser(TLFunction):
	ID = 0xca30a5b1

	def get_structure(self):
		return ("id", InputUser()),


TLRegister.register(getFullUser)
