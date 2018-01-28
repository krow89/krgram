from krgram.tl.api.types.globals import InputUser
from krgram.tl.types import *


class getStatuses(TLFunction):
	ID = 0xc4a353ee


TLRegister.register(getStatuses)


class getContacts(TLFunction):
	ID = 0x22c6aa08

	def get_structure(self):
		return ("hash", TL_string()),


TLRegister.register(getContacts)


class importContacts(TLFunction):
	ID = 0xda30b32d

	def get_structure(self):
		return ("contacts", Vector()), ("replace", Bool()),


TLRegister.register(importContacts)


class deleteContact(TLFunction):
	ID = 0x8e953744

	def get_structure(self):
		return ("id", InputUser()),


TLRegister.register(deleteContact)


class deleteContacts(TLFunction):
	ID = 0x59ab389e

	def get_structure(self):
		return ("id", Vector()),


TLRegister.register(deleteContacts)


class block(TLFunction):
	ID = 0x332b49fc

	def get_structure(self):
		return ("id", InputUser()),


TLRegister.register(block)


class unblock(TLFunction):
	ID = 0xe54100bd

	def get_structure(self):
		return ("id", InputUser()),


TLRegister.register(unblock)


class getBlocked(TLFunction):
	ID = 0xf57c350f

	def get_structure(self):
		return ("offset", TL_int()), ("limit", TL_int()),


TLRegister.register(getBlocked)


class exportCard(TLFunction):
	ID = 0x84e53737


TLRegister.register(exportCard)


class importCard(TLFunction):
	ID = 0x4fe196fe

	def get_structure(self):
		return ("export_card", Vector()),


TLRegister.register(importCard)


class search(TLFunction):
	ID = 0x11f812d8

	def get_structure(self):
		return ("q", TL_string()), ("limit", TL_int()),


TLRegister.register(search)
