from krgram import Bytes

class IByteStream(object):
	def write(self, data):
		pass

	def read(self, count):
		pass


class QueueByteStream(IByteStream):

	def __init__(self, src=None):
		self._data= Bytes()
		if src is not None:
			if isinstance(src, QueueByteStream):
				self._copy(src)
			elif isinstance(src, Bytes):
				self.clear()
				self.write(src)

	def clear(self):
		if len(self._data) != 0:
			del self._data
			self._data = Bytes()

	def read(self, count=0):
		len_data= len( self._data )
		# TODO: raise an error??
		if count==0:
			count= len(self)
		if len_data==0:
			raise Exception("read from empty stream")
		to_read= min(count, len_data)
		ret= self._data[:to_read]
		self._data= self._data[to_read:]
		return ret

	def write(self, data):
		self._data += data

	def __len__(self):
		return len(self._data)

	def __repr__(self):
		return repr(self._data)

	def _copy(self, src):
		self.clear()
		self.write( src._data[:] )


class StackByteStream(IByteStream):
	pass