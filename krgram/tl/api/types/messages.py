from krgram.tl.api.types.globals import EncryptedFile, Message
from krgram.tl.core_types.native import TL_bytes
from krgram.tl.types import *


class dialogs(TLConstructor):
	ID = 0x15ba6c40

	def get_structure(self):
		return ("dialogs", Vector()), ("messages", Vector()), ("chats", Vector()), ("users", Vector()),


class dialogsSlice(TLConstructor):
	ID = 0x71e094f3

	def get_structure(self):
		return ("count", TL_int()), ("dialogs", Vector()), ("messages", Vector()),\
			   ("chats", Vector()), ("users", Vector()),


class messages(TLConstructor):
	ID = 0x8c718e87

	def get_structure(self):
		return ("messages", Vector()), ("chats", Vector()), ("users", Vector()),


class messagesSlice(TLConstructor):
	ID = 0xb446ae3

	def get_structure(self):
		return ("count", TL_int()), ("messages", Vector()), ("chats", Vector()), ("users", Vector()),


class statedMessages(TLConstructor):
	ID = 0x969478bb

	def get_structure(self):
		return ("messages", Vector()), ("chats", Vector()), ("users", Vector()), ("pts", TL_int()), ("seq", TL_int()),


class statedMessagesLinks(TLConstructor):
	ID = 0x3e74f5c6

	def get_structure(self):
		return ("messages", Vector()), ("chats", Vector()), ("users", Vector()), ("links", Vector()), (
		"pts", TL_int()), ("seq", TL_int()),


class statedMessage(TLConstructor):
	ID = 0xd07ae726

	def get_structure(self):
		return ("message", Message()), ("chats", Vector()), ("users", Vector()), ("pts", TL_int()), ("seq", TL_int()),


class statedMessageLink(TLConstructor):
	ID = 0xa9af2881

	def get_structure(self):
		return ("message", Message()), ("chats", Vector()), ("users", Vector()), \
			   ("links", Vector()), ("pts", TL_int()), ("seq", TL_int()),


class sentMessage(TLConstructor):
	ID = 0xd1f4d35c

	def get_structure(self):
		return ("id", TL_int()), ("date", TL_int()), ("pts", TL_int()), ("seq", TL_int()),


class sentMessageLink(TLConstructor):
	ID = 0xe9db4a3f

	def get_structure(self):
		return ("id", TL_int()), ("date", TL_int()), ("pts", TL_int()), ("seq", TL_int()), ("links", Vector()),


class chats(TLConstructor):
	ID = 0x8150cbd8

	def get_structure(self):
		return ("chats", Vector()), ("users", Vector()),


class chatFull(TLConstructor):
	ID = 0xe5d7d19c

	def get_structure(self):
		return ("full_chat", ChatFull()), ("chats", Vector()), ("users", Vector()),


class affectedHistory(TLConstructor):
	ID = 0xb7de36f2

	def get_structure(self):
		return ("pts", TL_int()), ("seq", TL_int()), ("offset", TL_int()),


class dhConfigNotModified(TLConstructor):
	ID = 0xc0e24635

	def get_structure(self):
		return ("random", TL_bytes()),


class dhConfig(TLConstructor):
	ID = 0x2c221edd

	def get_structure(self):
		return ("g", TL_int()), ("p", TL_bytes()), ("version", TL_int()), ("random", TL_bytes()),


class sentEncryptedMessage(TLConstructor):
	ID = 0x560f8935

	def get_structure(self):
		return ("date", TL_int()),


class sentEncryptedFile(TLConstructor):
	ID = 0x9493ff32

	def get_structure(self):
		return ("date", TL_int()), ("file", EncryptedFile()),


class StatedMessages(TLConstructedType):
	CONSTRUCTORS_CLASSES = statedMessages, statedMessagesLinks,


TLRegister.register(StatedMessages)


class SentEncryptedMessage(TLConstructedType):
	CONSTRUCTORS_CLASSES = sentEncryptedMessage, sentEncryptedFile,


TLRegister.register(SentEncryptedMessage)


class Messages(TLConstructedType):
	CONSTRUCTORS_CLASSES = messages, messagesSlice,


TLRegister.register(Messages)


class Chats(TLConstructedType):
	CONSTRUCTORS_CLASSES = chats,


TLRegister.register(Chats)


class SentMessage(TLConstructedType):
	CONSTRUCTORS_CLASSES = sentMessage, sentMessageLink,


TLRegister.register(SentMessage)


class AffectedHistory(TLConstructedType):
	CONSTRUCTORS_CLASSES = affectedHistory,


TLRegister.register(AffectedHistory)


class ChatFull(TLConstructedType):
	CONSTRUCTORS_CLASSES = chatFull,


TLRegister.register(ChatFull)


class Dialogs(TLConstructedType):
	CONSTRUCTORS_CLASSES = dialogs, dialogsSlice,


TLRegister.register(Dialogs)


class DhConfig(TLConstructedType):
	CONSTRUCTORS_CLASSES = dhConfigNotModified, dhConfig,


TLRegister.register(DhConfig)


class StatedMessage(TLConstructedType):
	CONSTRUCTORS_CLASSES = statedMessage, statedMessageLink,


TLRegister.register(StatedMessage)
