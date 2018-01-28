from krgram.tl.api.types.globals import InputFileLocation
from krgram.tl.types import *


class saveFilePart(TLFunction):
	ID = 0xb304a621

	def get_structure(self):
		return ("file_id", TL_long()), ("file_part", TL_int()), ("bytes", TL_bytes()),


TLRegister.register(saveFilePart)


class getFile(TLFunction):
	ID = 0xe3a6cfb5

	def get_structure(self):
		return ("location", InputFileLocation()), ("offset", TL_int()), ("limit", TL_int()),


TLRegister.register(getFile)


class saveBigFilePart(TLFunction):
	ID = 0xde7b673d

	def get_structure(self):
		return ("file_id", TL_long()), ("file_part", TL_int()), ("file_total_parts", TL_int()), ("bytes", TL_bytes()),


TLRegister.register(saveBigFilePart)
