from krgram import Bytes
from krgram.tl.base import TLSerializable, TLBasicTypeSerializer, TLRegister
from krgram.tl.stream import TLBytesStream
from krgram.tl.types import TL_long, TL_int
from krgram.utils.stream import QueueByteStream


class BaseMsg(object):
	"""
	Encapsule a basic message
	"""

	def __init__(self, auth_key_id, content):
		self.auth_key_id = auth_key_id
		self.content = content

	def get_auth_key_id(self):
		return self.auth_key_id

	def get_content(self):
		return self.content

	def serialize(self):
		pass

	def deserialize(self, bytes_raw):
		pass


class PlainMsg(BaseMsg):
	"""
	Represent an unencrypted message where auth_key_id is always 0
	"""

	def __init__(self, msg_id, content):
		super(PlainMsg, self).__init__(0, content)
		self.msg_id = msg_id

	def serialize(self):
		msg_data= self.get_content()
		if isinstance(msg_data, TLSerializable):
			msg_data= msg_data.serialize()
		msg_len= len(msg_data)
		out= Bytes( 8 + 8 + 4 + msg_len )
		out[0:8]= Bytes('\00' * 8)

		out[8:16]= TLBasicTypeSerializer.serialize_long(self.msg_id, False) #Bytes.from_int( self.msg_id, 8, big_endian=False, signed=False )
		out[16:20]= TLBasicTypeSerializer.serialize_int32(msg_len, False)#Bytes.from_int( msg_len, 4, big_endian=False, signed=False )
		out[20:]= msg_data
		return out

	def deserialize(self, stream):
		if not isinstance(stream, QueueByteStream):
			stream = QueueByteStream(stream)
		# TODO: add checks
		self.auth_key_id = TLBasicTypeSerializer.deserialize_long(stream) #TL_long().deserialize_from(stream).get()
		self.msg_id = TLBasicTypeSerializer.deserialize_long(stream, False)
		msg_len = TLBasicTypeSerializer.deserialize_int32(stream, False)
		serialized_content = stream.read(msg_len)
		func_id_content = TLBasicTypeSerializer.deserialize_int32(serialized_content[:4])
		func_class = TLRegister.get(func_id_content)
		if func_class is not None:
			self.content = func_class()
			self.content.deserialize_from(TLBytesStream(serialized_content))
		else:
			self.content = None # this is bad
		return self



class EncryptedMsgData:
	def __init__(self, salt, session_id, message_id, seq_no, message_data):
		self.salt = salt
		self.session_id = session_id
		self.message_id = message_id
		self.seq_no = seq_no
		self.data = message_data

	def serialize(self):
		bs = TLBytesStream()
		bs.write_tl(TL_long(self.salt), TL_long(self.session_id), TL_long(self.message_id))
		bs.write_tl(TL_int(self.seq_no))
		msg_len = len(self.data)
		bs.write_tl(TL_int(msg_len))
		bs.write(self.data)
		tot_len = 8+8+8+4+4+msg_len
		padding_count = 16 - (tot_len % 16)
		if padding_count < 12:
			padding_count += 16
		padding = Bytes('\x00'*padding_count)
		bs.write(padding)
		return bs.read()

	def deserialize(self, bytes_raw):
		TLS = TLBasicTypeSerializer
		stream = TLBytesStream(bytes_raw)
		self.salt= TLS.deserialize_long(stream) # TL_long().deserialize_from(stream)
		self.session_id = TLS.deserialize_long(stream) # TL_long().deserialize_from(stream)
		self.message_id = TLS.deserialize_long(stream) #TL_long().deserialize_from(stream)
		self.seq_no = TLS.deserialize_int32(stream) #TL_int().deserialize_from(stream)
		data_len = TLS.deserialize_int32(stream) #TL_int().deserialize_from(stream)
		data = stream.read(data_len)
		self.data = data
		# TODO: remove padding reading
		padding_count = 16 - (data_len % 16)
		if padding_count < 12:
			padding_count += 16
		stream.read(padding_count) # read padding
		return self




class EncryptedMsg(BaseMsg):
	def __init__(self, auth_key_id, msg_key, enc_msg):
		super(EncryptedMsg, self).__init__(auth_key_id, enc_msg)
		self.msg_key= msg_key

	def get_encrypted_message(self):
		return self.get_content()

	def set_encrypted_message(self, enc_message):
		self.content = enc_message

	def get_message_key(self):
		return self.msg_key

	def serialize(self):
		bs = TLBytesStream()
		return bs.write_tl(self.auth_key_id, self.msg_key, self.get_encrypted_message()).read()

	def deserialize(self, bytes_raw):
		stream = TLBytesStream(bytes_raw)
		self.auth_key_id, self.msg_key =  stream.read(8), stream.read(16)
		enc_data = stream.read()#EncryptedMsgData(None, None, None, None, None).deserialize_from(stream)
		self.set_encrypted_message(enc_data)
		return self
