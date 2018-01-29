from krgram.tl.api.types.globals import InputPeer, InputUser, InputEncryptedChat, InputChatPhoto, InputMedia, \
	SendMessageAction, MessagesFilter, InputEncryptedFile
from krgram.tl.core_types.native import TL_long, TL_string, TL_bytes
from krgram.tl.types import *


class getMessages(TLFunction):
	ID = 0x4222fa74

	def get_structure(self):
		return ("id", Vector()),


TLRegister.register(getMessages)


class getDialogs(TLFunction):
	ID = 0xeccf1df6

	def get_structure(self):
		return ("offset", TL_int()), ("max_id", TL_int()), ("limit", TL_int()),


TLRegister.register(getDialogs)


class getHistory(TLFunction):
	ID = 0x92a1df2f

	def get_structure(self):
		return ("peer", InputPeer()), ("offset", TL_int()), ("max_id", TL_int()), ("limit", TL_int()),


TLRegister.register(getHistory)


class search(TLFunction):
	ID = 0x7e9f2ab

	def get_structure(self):
		return ("peer", InputPeer()), ("q", TL_string()), ("filter", MessagesFilter()), \
			   ("min_date", TL_int()), ("max_date", TL_int()), ("offset", TL_int()), \
			   ("max_id", TL_int()), ("limit", TL_int()),


TLRegister.register(search)


class readHistory(TLFunction):
	ID = 0xeed884c6

	def get_structure(self):
		return ("peer", InputPeer()), ("max_id", TL_int()), ("offset", TL_int()), ("read_contents", Bool()),


TLRegister.register(readHistory)


class deleteHistory(TLFunction):
	ID = 0xf4f8fb61

	def get_structure(self):
		return ("peer", InputPeer()), ("offset", TL_int()),


TLRegister.register(deleteHistory)


class deleteMessages(TLFunction):
	ID = 0x14f2dd0a

	def get_structure(self):
		return ("id", Vector()),


TLRegister.register(deleteMessages)


class receivedMessages(TLFunction):
	ID = 0x28abcb68

	def get_structure(self):
		return ("max_id", TL_int()),


TLRegister.register(receivedMessages)


class setTyping(TLFunction):
	ID = 0xa3825e50

	def get_structure(self):
		return ("peer", InputPeer()), ("action", SendMessageAction()),


TLRegister.register(setTyping)


class sendMessage(TLFunction):
	ID = 0x4cde0aab

	def get_structure(self):
		return ("peer", InputPeer()), ("message", TL_string()), ("random_id", TL_long()),


TLRegister.register(sendMessage)


class sendMedia(TLFunction):
	ID = 0xa3c85d76

	def get_structure(self):
		return ("peer", InputPeer()), ("media", InputMedia()), ("random_id", TL_long()),


TLRegister.register(sendMedia)


class forwardMessages(TLFunction):
	ID = 0x514cd10f

	def get_structure(self):
		return ("peer", InputPeer()), ("id", Vector()),


TLRegister.register(forwardMessages)


class reportSpam(TLFunction):
	ID = 0xcf1592db

	def get_structure(self):
		return ("peer", InputPeer()),


TLRegister.register(reportSpam)


class hideReportSpam(TLFunction):
	ID = 0xa8f1709b

	def get_structure(self):
		return ("peer", InputPeer()),


TLRegister.register(hideReportSpam)


class getPeerSettings(TLFunction):
	ID = 0x3672e09c

	def get_structure(self):
		return ("peer", InputPeer()),


TLRegister.register(getPeerSettings)


class getChats(TLFunction):
	ID = 0x3c6aa187

	def get_structure(self):
		return ("id", Vector()),


TLRegister.register(getChats)


class getFullChat(TLFunction):
	ID = 0x3b831c66

	def get_structure(self):
		return ("chat_id", TL_int()),


TLRegister.register(getFullChat)


class editChatTitle(TLFunction):
	ID = 0xb4bc68b5

	def get_structure(self):
		return ("chat_id", TL_int()), ("title", TL_string()),


TLRegister.register(editChatTitle)


class editChatPhoto(TLFunction):
	ID = 0xd881821d

	def get_structure(self):
		return ("chat_id", TL_int()), ("photo", InputChatPhoto()),


TLRegister.register(editChatPhoto)


class addChatUser(TLFunction):
	ID = 0x2ee9ee9e

	def get_structure(self):
		return ("chat_id", TL_int()), ("user_id", InputUser()), ("fwd_limit", TL_int()),


TLRegister.register(addChatUser)


class deleteChatUser(TLFunction):
	ID = 0xc3c5cd23

	def get_structure(self):
		return ("chat_id", TL_int()), ("user_id", InputUser()),


TLRegister.register(deleteChatUser)


class createChat(TLFunction):
	ID = 0x419d9aee

	def get_structure(self):
		return ("users", Vector()), ("title", TL_string()),


TLRegister.register(createChat)


class forwardMessage(TLFunction):
	ID = 0x3f3f4f2

	def get_structure(self):
		return ("peer", InputPeer()), ("id", TL_int()), ("random_id", TL_long()),


TLRegister.register(forwardMessage)


class getDhConfig(TLFunction):
	ID = 0x26cf8950

	def get_structure(self):
		return ("version", TL_int()), ("random_length", TL_int()),


TLRegister.register(getDhConfig)


class requestEncryption(TLFunction):
	ID = 0xf64daf43

	def get_structure(self):
		return ("user_id", InputUser()), ("random_id", TL_int()), ("g_a", TL_bytes()),


TLRegister.register(requestEncryption)


class acceptEncryption(TLFunction):
	ID = 0x3dbc0415

	def get_structure(self):
		return ("peer", InputEncryptedChat()), ("g_b", TL_bytes()), ("key_fingerprint", TL_long()),


TLRegister.register(acceptEncryption)


class discardEncryption(TLFunction):
	ID = 0xedd923c5

	def get_structure(self):
		return ("chat_id", TL_int()),


TLRegister.register(discardEncryption)


class setEncryptedTyping(TLFunction):
	ID = 0x791451ed

	def get_structure(self):
		return ("peer", InputEncryptedChat()), ("typing", Bool()),


TLRegister.register(setEncryptedTyping)


class readEncryptedHistory(TLFunction):
	ID = 0x7f4b690a

	def get_structure(self):
		return ("peer", InputEncryptedChat()), ("max_date", TL_int()),


TLRegister.register(readEncryptedHistory)


class sendEncrypted(TLFunction):
	ID = 0xa9776773

	def get_structure(self):
		return ("peer", InputEncryptedChat()), ("random_id", TL_long()), ("data", TL_bytes()),


TLRegister.register(sendEncrypted)


class sendEncryptedFile(TLFunction):
	ID = 0x9a901b66

	def get_structure(self):
		return ("peer", InputEncryptedChat()), ("random_id", TL_long()), ("data", TL_bytes()), (
		"file", InputEncryptedFile()),


TLRegister.register(sendEncryptedFile)


class sendEncryptedService(TLFunction):
	ID = 0x32d439a4

	def get_structure(self):
		return ("peer", InputEncryptedChat()), ("random_id", TL_long()), ("data", TL_bytes()),


TLRegister.register(sendEncryptedService)


class receivedQueue(TLFunction):
	ID = 0x55a5bb66

	def get_structure(self):
		return ("max_qts", TL_int()),


TLRegister.register(receivedQueue)


class reportEncryptedSpam(TLFunction):
	ID = 0x4b0c8c0f

	def get_structure(self):
		return ("peer", InputEncryptedChat()),


TLRegister.register(reportEncryptedSpam)


class readMessageContents(TLFunction):
	ID = 0x354b5bc2

	def get_structure(self):
		return ("id", Vector()),


TLRegister.register(readMessageContents)
