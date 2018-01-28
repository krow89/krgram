import socket

from krgram.utils.bytes import Bytes
from krgram.utils.stream import QueueByteStream, IByteStream

_debug= True

class TCPByteStream(IByteStream):
	"""
	Represents a TCP connection as a bidirectional stream (readable/writable)

	Example usage::

		tcpstream = TCPByteStream(host, port)
		tcpstream.write("Hi, this a message from client")
		tcpstream.write("and asterisc close message*")
		# now the message is in a buffer. We must send it...
		tcpstream.send()
		# ... and read server response. Here
		msg_len = int(tcpstream.read(4))
		tcp_stream.read(msg_len)
	"""

	_DEF_READ_TIMEOUT = 10

	def __init__(self, host, port):
		super(TCPByteStream, self).__init__()
		self.host= host
		self.port= port
		self.sock= socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self.sock.settimeout(self._DEF_READ_TIMEOUT)
		# server data buffer
		self._in = QueueByteStream()
		# client data buffer
		self._out = QueueByteStream()

	def open(self):
		self.sock.connect( (self.host, self.port) )

	def read(self, count=0):
		"""
		Read data from buffer (or/and tcp socket if necessary). If count is 0, reading will be only
		from memory buffer (without reading from socket) and return all buffer content

		:param count: bytes to read
		:return: readed bytes
		"""
		if count < 0:
			raise ValueError("count must be an integer >= 0")
		if count == 0:
			return self._in.read(0)
		buff_data_count = len(self._in)
		if buff_data_count < count:
			# size is minimum size
			if count > 4096:
				size = 4096 << 1  # TODO: size MUST be nearest greater pow of 2
			else:
				size = 4096
			self._read_remote_chunk(size)
			buff_data_count = len(self._in)
			if buff_data_count < count:
				self.close()
				raise Exception("server not sended bytes count requested")
		data = self._in.read(count)
		return data

	def read_all(self, reader):
		# TODO: implement me
		raise NotImplementedError()

	def write(self, data):
		#self.sock.send( data )
		self._out.write(data)
		print repr(Bytes(data))

	def send(self):
		data = self._out.read()
		self.sock.sendall(data)
		print repr(data)

	def _read_remote_chunk(self, chunk_size):
		data = Bytes(self.sock.recv(chunk_size))
		self._in.write(data)
		return len(data)

	'''def write_byte(self, b):
		self.write(b)

	def write_int(self, n, size=4, big_endian=False):
		self.write(Bytes.from_int(n, size, big_endian))

	def read_byte(self):
		return self.read(1)

	def read_int(self, size=4, big_endian=False, signed=False):
		d= self.read(size)
		return Bytes(d).to_int(big_endian, signed)'''


	def close(self):
		if self.sock is not None:
			self.sock.close()
