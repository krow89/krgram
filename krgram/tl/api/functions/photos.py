from krgram.tl.api.types.globals import InputFile, InputPhotoCrop, InputGeoPoint, InputPhoto, InputUser
from krgram.tl.types import *


class updateProfilePhoto(TLFunction):
	ID = 0xeef579a0

	def get_structure(self):
		return ("id", InputPhoto()), ("crop", InputPhotoCrop()),


TLRegister.register(updateProfilePhoto)


class uploadProfilePhoto(TLFunction):
	ID = 0xd50f9c88

	def get_structure(self):
		return ("file", InputFile()), ("caption", TL_string()), ("geo_point", InputGeoPoint()), (
		"crop", InputPhotoCrop()),


TLRegister.register(uploadProfilePhoto)


class deletePhotos(TLFunction):
	ID = 0x87cf7f2f

	def get_structure(self):
		return ("id", Vector()),


TLRegister.register(deletePhotos)


class getUserPhotos(TLFunction):
	ID = 0xb7ee553c

	def get_structure(self):
		return ("user_id", InputUser()), ("offset", TL_int()), ("max_id", TL_int()), ("limit", TL_int()),


TLRegister.register(getUserPhotos)
