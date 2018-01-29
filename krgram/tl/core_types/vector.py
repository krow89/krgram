from krgram.tl.base import *
from krgram.tl.core_types.native import TL_int


class vector(TLConstructor):
	ID = 0x1cb5c415

	def __init__(self, item_creator):
		self._item_creator= item_creator
		self._vector= TL_vector(item_creator)
		super(vector, self).__init__()

	def get(self):
		return self._vector.get()

	def set_item_creator(self, item_creator):
		self._item_creator = item_creator

	def serialize(self):
		return self._vector.serialize()

	def deserialize_from(self, stream):
		return self._vector.deserialize_from(stream)


class Vector(TLConstructedType):
	CONSTRUCTORS_CLASSES = (vector,)

	def get(self):
		ctor = super(Vector, self).get()
		if ctor is None:
			return None
		elif isinstance(ctor, vector):
			return ctor.get()
		else: return None


class TL_vector(TLBaseType):
	def __init__(self, item_creator):
		self._item_creator= item_creator
		self._item_class= item_creator().__class__
		super(TL_vector, self).__init__([])

	def set_item_creator(self, item_creator):
		self._item_creator = item_creator

	def set(self, value):
		if not isinstance(value, (tuple,list)):
			raise ValueError("tuple or list accepted only")
		# TODO: add check for item type
		super(TL_vector, self).set(value)

	def serialize(self):
		items = self.get()
		count = len(items)
		ret = TL_int(count).serialize()
		for i in items:
			ret += i.serialize()
		return ret

	def deserialize_from(self, stream):
		count = TL_int().deserialize_from(stream).get()
		items= []
		for i in range(count):
			item= self._item_creator()
			item.deserialize_from(stream)
			items.append(item.get())
		self.set(items)
		return self