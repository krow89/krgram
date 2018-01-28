from krgram.tl.types import *


class fileUnknown(TLConstructor):
	ID = 0xaa963b05


class filePartial(TLConstructor):
	ID = 0x40bc6f52


class fileJpeg(TLConstructor):
	ID = 0x7efe0e


class fileGif(TLConstructor):
	ID = 0xcae1aadf


class filePng(TLConstructor):
	ID = 0xa4f63c0


class filePdf(TLConstructor):
	ID = 0xae1e508d


class fileMp3(TLConstructor):
	ID = 0x528a0677


class fileMov(TLConstructor):
	ID = 0x4b09ebbc


class fileMp4(TLConstructor):
	ID = 0xb3cea0e4


class fileWebp(TLConstructor):
	ID = 0x1081464c


class FileType(TLConstructedType):
	CONSTRUCTORS_CLASSES = fileUnknown, filePartial, fileJpeg, fileGif, filePng, \
						   filePdf, fileMp3, fileMov, fileMp4, fileWebp,


TLRegister.register(FileType)
