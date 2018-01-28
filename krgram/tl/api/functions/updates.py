from krgram.tl.types import *


class getState(TLFunction):
	ID = 0xedd4882a


TLRegister.register(getState)


class getDifference(TLFunction):
	ID = 0xa041495

	def get_structure(self):
		return ("pts", TL_int()), ("date", TL_int()), ("qts", TL_int()),


TLRegister.register(getDifference)
