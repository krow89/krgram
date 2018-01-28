from krgram.tl.api.types.globals import User
from krgram.tl.types import *


class foreignLinkUnknown(TLConstructor):
	ID = 0x133421f8


class foreignLinkRequested(TLConstructor):
	ID = 0xa7801f47

	def get_structure(self):
		return ("has_phone", Bool()),


class foreignLinkMutual(TLConstructor):
	ID = 0x1bea8ce1


class myLinkEmpty(TLConstructor):
	ID = 0xd22a1c60


class myLinkRequested(TLConstructor):
	ID = 0x6c69efee

	def get_structure(self):
		return ("contact", Bool()),


class myLinkContact(TLConstructor):
	ID = 0xc240ebd9


class contactsNotModified(TLConstructor):
	ID = 0xb74ba9d2


class contacts(TLConstructor):
	ID = 0x6f8b8cb2

	def get_structure(self):
		return ("contacts", Vector()), ("users", Vector()),


class importedContacts(TLConstructor):
	ID = 0xad524315

	def get_structure(self):
		return ("imported", Vector()), ("retry_contacts", Vector()), ("users", Vector()),


class blocked(TLConstructor):
	ID = 0x1c138d15

	def get_structure(self):
		return ("blocked", Vector()), ("users", Vector()),


class blockedSlice(TLConstructor):
	ID = 0x900802a1

	def get_structure(self):
		return ("count", TL_int()), ("blocked", Vector()), ("users", Vector()),


class found(TLConstructor):
	ID = 0x566000e

	def get_structure(self):
		return ("results", Vector()), ("users", Vector()),


class ImportedContacts(TLConstructedType):
	CONSTRUCTORS_CLASSES = importedContacts,


TLRegister.register(ImportedContacts)


class Found(TLConstructedType):
	CONSTRUCTORS_CLASSES = found,


TLRegister.register(Found)


class Blocked(TLConstructedType):
	CONSTRUCTORS_CLASSES = blocked, blockedSlice,


TLRegister.register(Blocked)


class Contacts(TLConstructedType):
	CONSTRUCTORS_CLASSES = contactsNotModified, contacts,


TLRegister.register(Contacts)


class MyLink(TLConstructedType):
	CONSTRUCTORS_CLASSES = myLinkEmpty, myLinkRequested, myLinkContact,


TLRegister.register(MyLink)


class link(TLConstructor):
	ID = 0xeccea3f5

	def get_structure(self):
		return ("my_link", MyLink()), ("foreign_link", ForeignLink()), ("user", User()),


class Link(TLConstructedType):
	CONSTRUCTORS_CLASSES = link,


TLRegister.register(Link)


class ForeignLink(TLConstructedType):
	CONSTRUCTORS_CLASSES = foreignLinkUnknown, foreignLinkRequested, foreignLinkMutual,


TLRegister.register(ForeignLink)
