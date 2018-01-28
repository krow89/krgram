import os
import time

from krgram.tl.base import TLSerializable
from krgram.utils.bytes import Bytes


class MsgId(TLSerializable):
	def __init__(self, delta = 0.0):
		self.delta = float(delta)
		self.curr = self()

	def __call__(self):
		now = time.time() + self.delta
		now_sec = int(now)
		frac = int((now - float(now_sec))*1000.0)
		msg_id = 0x0L | (now_sec << 32) | (frac << 3)
		return msg_id

	def serialize(self):
		return Bytes.from_int( self.curr, 8, False, False )

	def deserialize_from(self, stream):
		self.curr = Bytes(stream.read(8)).to_int(False, False)


class MsgSeqNo(TLSerializable):
	def __init__(self ):
		self._content_related_sended = 0
		self._curr = 0

	def __call__(self, content_related = True):
		seq_no = self._content_related_sended*2
		if content_related:
			seq_no += 1
			self._content_related_sended += 1
		return seq_no

	def serialize(self):
		return Bytes.from_int(self._curr, 4, False, False)

	def deserialize_from(self, stream):
		self._curr = Bytes(stream.read(4)).to_int(False, False)
		self._content_related_sended = self._curr // 2


class SessionId(TLSerializable):
	def __init__(self, sid):
		if sid is None:
			raise ValueError("Session ID cannot be None")
		else:
			if isinstance(sid, Bytes):
				self._id = sid.to_int()
			else:
				self._id = int(sid)

	@staticmethod
	def create():
		sid = Bytes(os.urandom(8))
		return SessionId(sid)

	def __call__(self):
		return self.serialize()

	def serialize(self):
		return Bytes.from_int(self._id, 8, False, False)

	def deserialize_from(self, stream):
		self._id = Bytes(stream.read(8)).to_int(False, False)
