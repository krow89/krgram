from krgram import Bytes
from krgram.tl.base import TLSerializable
from krgram.utils.stream import QueueByteStream


class TLBytesStream(QueueByteStream):

	def __init__(self, src=None):
		super(TLBytesStream, self).__init__(src)

	def write_tl(self, *tlobjs):
		for tlobj in tlobjs:
			if isinstance(tlobj, TLSerializable):
				self.write(tlobj.serialize())
			elif isinstance(tlobj, Bytes):
				self.write(tlobj)
			else:
				raise TypeError("all items must be TLBaseType or Bytes subclass instances")
		return self

