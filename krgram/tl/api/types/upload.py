from krgram.tl.api.types import storage
from krgram.tl.core_types.native import TL_bytes
from krgram.tl.types import *


# noinspection PyShadowingBuiltins
class file(TLConstructor):
	ID = 0x96a18d5

	def get_structure(self):
		return ("type", storage.FileType()), ("mtime", TL_int()), ("bytes", TL_bytes()),


class File(TLConstructedType):
	CONSTRUCTORS_CLASSES = file,


TLRegister.register(File)
