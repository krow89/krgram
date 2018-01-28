from krgram.tl.types import *


class photos(TLConstructor):
	ID = 0x8dca6aa5

	def get_structure(self):
		return ("photos", Vector()), ("users", Vector()),


class photosSlice(TLConstructor):
	ID = 0x15051f54

	def get_structure(self):
		return ("count", TL_int()), ("photos", Vector()), ("users", Vector()),


class photo(TLConstructor):
	ID = 0x20212ca8

	def get_structure(self):
		return ("photo", Photo()), ("users", Vector()),


class Photos(TLConstructedType):
	CONSTRUCTORS_CLASSES = photos, photosSlice,


TLRegister.register(Photos)


class Photo(TLConstructedType):
	CONSTRUCTORS_CLASSES = photo,


TLRegister.register(Photo)
