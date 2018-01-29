from krgram.tl.base import *


class boolTrue(TLConstructor):
	ID = 0x997275b5

	def get(self):
		return True


class boolFalse(TLConstructor):
	ID = 0xbc799737

	def get(self):
		return False


class Bool(TLConstructedType):
	CONSTRUCTORS_CLASSES = (boolTrue, boolFalse)


TLRegister.register_constructed_types(Bool)
