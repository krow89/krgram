from krgram import Bytes
from krgram.tl.core_types.native import TL_int, TL_string


class TL_int128(TL_int):
	def __init__(self, v=0):
		super(TL_int128, self).__init__(v, signed=False)

	def serialize(self):
		v = self.get()
		return Bytes.from_int(v, 16, True)

	def deserialize_from(self, stream):
		self.set(Bytes(stream.read(16)).to_int(True))
		return self


class TL_int256(TL_int):
	def serialize(self):
		return Bytes.from_int(self.get(), 32, True, signed=self._signed)

	def deserialize_from(self, stream):
		self.set(Bytes(stream.read(32)).to_int(True))
		return self


class TL_int_as_string(TL_int):
	def __init__(self, i=0, size=4, signed=False):
		super(TL_int_as_string, self).__init__(i, signed=signed)
		self._byte_len = size

	def serialize(self):
		itos = Bytes.from_int(self.get(), self._byte_len, True, self._signed)
		tls = TL_string(itos)
		return tls.serialize()

	def deserialize_from(self, stream):
		tls = TL_string()
		tls.deserialize_from(stream)
		self.set(Bytes(tls.get()).to_int(True, self._signed))
		return self


