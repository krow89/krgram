from krgram import Bytes
from krgram.mtproto.errors import MTProtoFatalError
from krgram.mtproto.message import BaseMsg
from krgram.mtproto.tcp import TCPByteStream
from krgram.tl.stream import TLBytesStream


class BaseMTProtoConnection(object):
	"""
	Abstract class for represent connection that understand message concept
	"""

	def __init__(self):
		self._tcp= None

	def open(self, host, port):
		if self._tcp is not None:
			self._tcp.close()
		self._tcp= TCPByteStream(host, port)
		self._tcp.open()

	def send_raw(self, raw_bytes):
		raise NotImplementedError("Abstract method not callable")

	def read_raw(self):
		raise NotImplementedError()

	def _get_tcp_stream(self):
		return self._tcp

	def send_message(self, msg):
		if not isinstance(msg, BaseMsg):
			raise TypeError("Only " + BaseMsg.__class__.__name__ + " instances allowed")
		ser_msg = msg.serialize()
		self.send_raw(ser_msg)
		self._tcp.send()

	def read_message_to(self, msg_obj):
		if not isinstance(msg_obj, BaseMsg):
			raise TypeError("Only " + BaseMsg.__class__.__name__ + " instances allowed")
		msg_stream = self.read_raw()
		msg_obj.deserialize(msg_stream)
		return msg_obj

	def close(self):
		self._tcp.close()


class MTProtoAbridgedConnection(BaseMTProtoConnection):
	"""
	Abridged connection type
	"""

	def __init__(self):
		super(self.__class__, self).__init__()
		self._send_abridged_flag= True

	def close(self):
		super(self.__class__, self).close()
		self._send_abridged_flag= True

	def send_raw(self, data):
		msg_len = len(data) >> 2
		tcp_stream = self._get_tcp_stream()
		if self._send_abridged_flag:
			tcp_stream.write(chr(0xef))
			self._send_abridged_flag = False
		if msg_len < 127:
			tcp_stream.write(Bytes.from_int(msg_len, 1, False))
		else:
			tcp_stream.write(chr(0x7f))
			tcp_stream.write( Bytes.from_int(msg_len, 3, False) )
		tcp_stream.write(data)

	def read_raw(self):
		tcp_stream = self._get_tcp_stream()
		packet_len = ord(tcp_stream.read(1))
		if packet_len == 0x7f:
			packet_len = Bytes(self._tcp.read(3)).to_int(False, False)
		packet_len *= 4
		packet = self._tcp.read(packet_len)
		if packet == b"\x6c\xfe\xff\xff":
			raise MTProtoFatalError("Error -404 while reading message")
		stream = TLBytesStream(packet)
		return stream
