from krgram.tl.types import *


class state(TLConstructor):
	ID = 0xa56c2a3e

	def get_structure(self):
		return ("pts", TL_int()), ("qts", TL_int()), ("date", TL_int()), ("seq", TL_int()), ("unread_count", TL_int()),


class differenceEmpty(TLConstructor):
	ID = 0x5d75a138

	def get_structure(self):
		return ("date", TL_int()), ("seq", TL_int()),


class State(TLConstructedType):
	CONSTRUCTORS_CLASSES = state,


TLRegister.register(State)


class difference(TLConstructor):
	ID = 0xf49ca0

	def get_structure(self):
		return ("new_messages", Vector()), ("new_encrypted_messages", Vector()), ("other_updates", Vector()), \
			   ("chats", Vector()), ("users", Vector()), ("state", State()),


class differenceSlice(TLConstructor):
	ID = 0xa8fb1981

	def get_structure(self):
		return ("new_messages", Vector()), ("new_encrypted_messages", Vector()), ("other_updates", Vector()), \
			   ("chats", Vector()), ("users", Vector()), ("intermediate_state", State()),


class Difference(TLConstructedType):
	CONSTRUCTORS_CLASSES = differenceEmpty, difference, differenceSlice,


TLRegister.register(Difference)
