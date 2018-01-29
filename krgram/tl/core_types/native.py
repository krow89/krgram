from krgram import Bytes
from krgram.tl.base import *


class TL_int(TLBaseType):
	def __init__(self, v=0, signed=True):
		self._signed = signed
		super(TL_int, self).__init__(v)

	def set(self, v):
		if v is None:
			v= 0
		elif not isinstance(v, (int,long)):
			v= Bytes(v).to_int(False, self._signed)
		super(TL_int, self).set(v)

	def serialize(self):
		v= self.get()
		return TLBaseSerializer.serialize_int32(v, self._signed)

	def deserialize_from(self, stream):
		v = TLBaseSerializer.deserialize_int32(stream, self._signed)
		self.set(v)
		return self


class TL_long(TL_int):
	def serialize(self):
		v = self.get()
		return TLBaseSerializer.serialize_long(v, self._signed)

	def deserialize_from(self, stream):
		v = TLBaseSerializer.deserialize_long(stream, self._signed)
		self.set(v)
		return self


class TL_string(TLBaseType):
	def __init__(self, s=""):
		super(TL_string, self).__init__(s)

	def set(self, value):
		if not isinstance(value, (str,Bytes)):
			raise Exception()
		super(TL_string, self).set(value)

	def size(self):
		datal = len(self.get()) + 1
		return datal + (4-(datal%4))

	def serialize(self):
		b = TLBaseSerializer.serialize_string(self.get())
		return b

	def deserialize_from(self, stream):
		s = TLBaseSerializer.deserialize_string(stream)
		self.set(s)
		return self


class TL_bytes(TL_string):
	pass


class TL_double(TLBaseType):
	def __init__(self, value=0.0):
		super(TL_double, self).__init__(value)

	def serialize(self):
		return TLBaseSerializer.serialize_double(self.get())

	def deserialize_from(self, stream):
		d = TLBaseSerializer.deserialize_double(stream)
		self.set(d)
		return self