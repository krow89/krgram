from krgram import Bytes
from krgram.utils.stream import QueueByteStream


class TLBasicTypeSerializer:

	@staticmethod
	def serialize_int32(i, signed=True):
		return Bytes.from_int(i, 4, False, signed)

	@staticmethod
	def deserialize_int32(bs, signed=True):
		if isinstance(bs, QueueByteStream):
			raw = bs.read(4)
			return raw.to_int(False, signed)
		elif isinstance(bs, Bytes):
			return bs.to_int(False, signed)
		else:
			raise ValueError("bs must be a TLBytesStream or Bytes instance")

	@staticmethod
	def serialize_long(l, signed=True):
		return Bytes.from_int(l, 8, False, signed)

	@staticmethod
	def deserialize_long(bs, signed=True):
		if isinstance(bs, QueueByteStream):
			raw = bs.read(8)
			return raw.to_int(False, signed)
		elif isinstance(bs, Bytes):
			return bs.to_int(False, signed)
		else:
			raise ValueError("bs must be a TLBytesStream or Bytes instance")

	@staticmethod
	def serialize_string(s):
		slen = len(s)
		if slen < 254:
			pad_count = 4 - ((slen + 1) % 4)
			if pad_count == 4: pad_count = 0
			b = Bytes(slen + 1)
			b[0] = slen
			b[1:] = s
			if pad_count != 0:
				# TODO: fill with random data
				b += Bytes('\x00'*pad_count)
		else:
			pad_count = 4 - (slen % 4)
			if pad_count == 4: pad_count = 0
			b = Bytes(slen + 1)
			b[0] = 254
			b[1:4] = [slen % 256, (slen >> 8) % 256, (slen >> 16) % 256]
			b[4:] = s
			if pad_count != 0:
				b += Bytes('\x00'*pad_count)
		return b

	@staticmethod
	def deserialize_string(bs):
		stream = bs
		if isinstance(bs, Bytes):
			stream = QueueByteStream(bs)
		elif not isinstance(bs, QueueByteStream):
			raise ValueError("bs must be a Bytes or TLByteStream instance")
		h = ord(stream.read(1))
		readed = 1
		if h == 254:
			tri = stream.read(3)
			size = tri[0] + tri[1] * 256 + tri[2] * 256 * 256
			readed += 3
		else:
			size = h
		byte_str = stream.read(size)
		# dont forget to read padding
		readed += size
		pad = 4 - (readed % 4)
		if pad > 0 and pad != 4:
			stream.read(pad)
		return str(byte_str)

	@staticmethod
	def serialize_double(d):
		raise NotImplementedError()

	@staticmethod
	def deserialize_double(bs):
		raise NotImplementedError()


class TLSerializable(object):
	"""
	Interface that will implement all TL serializable objects
	"""

	def serialize(self):
		"""
		Serialize object

		Sub-classes will have to implement this method that return serialized form of object

		:return Bytes: serialized bytes of object
		"""
		raise NotImplementedError()

	def serialize_to(self, stream):
		ser = self.serialize()
		stream.write(ser)

	def deserialize_from(self, stream):
		raise NotImplementedError()


class TLBaseType(TLSerializable):

	def __init__(self, v):
		self._value = None
		self.set(v)

	def set(self, value):
		self._value = value

	def get(self):
		return self._value

	def serialize(self):
		raise NotImplementedError()

	def deserialize_from(self, stream):
		raise NotImplementedError()


class TLConstructedType(TLBaseType):
	CONSTRUCTORS_CLASSES = None

	def __init__(self, ctor=None):
		self._ref_ctor = ctor
		super(TLConstructedType, self).__init__(ctor)

	def set(self, ctor):
		if ctor is not None and not issubclass(ctor.__class__, self.CONSTRUCTORS_CLASSES):
			raise ValueError("ctor is not a valid constructor of this class")
		self._ref_ctor = ctor
		super(TLConstructedType, self).set(ctor)

	def serialize(self):
		value = self.get()
		if value is None:
			raise ValueError("Cannot serialize None Type")
		return value.serialize()

	def deserialize_from(self, stream):
		# check ids of subclasses
		oid = Bytes(stream.read(4)).to_int(False, False)
		ctor = self._ref_ctor
		assert ctor.ID == oid
		ctor.deserialize_from(stream)
		return self


class TLFunction(TLBaseType):
	ID = None

	def __init__(self, **params):
		if self.__class__.ID is None:
			raise ValueError("ID cannot be None")
		self._params_map = {}
		self._member_access_flag = False
		# noinspection PyTypeChecker
		self._params_ordered = self._check_struct(self.get_structure())
		super(TLFunction, self).__init__(params)
		self._member_access_flag = True

	def set(self, dict_obj):
		if dict_obj is None:
			return
		for k in dict_obj:
			if k in self._params_map:
				self._params_map[k].set(dict_obj[k])

	def get(self):
		return self.to_dict()

	def serialize(self):
		stream = Bytes.from_int(self.ID, 4, False, False)
		for pname in self._params_ordered:
			stream += self._params_map[pname].serialize()
		return stream

	def deserialize_from(self, stream):
		# noinspection PyUnusedLocal
		self_id = TLBasicTypeSerializer.deserialize_int32( stream.read(4) )
		# TODO: add check on retrieve id ????
		for pname in self._params_ordered:
			self._params_map[pname].deserialize_from(stream)
		return self

	def size(self):
		size = 0
		for m in self._params_ordered:
			size += m[1].size()
		return size

	def _check_struct(self, s):
		if s is None:
			s = tuple()
		elif len(s) == 2:
			s = (s,)
		pnames = []
		for p in s:
			if len(p) != 2:
				raise ValueError(
					"%s : member structure must be a 2 item tuple in (name,class) format" % (self.__class__,))
			if not isinstance(p[1], TLBaseType):
				raise ValueError("%s (%s) : class of member must be an subclass of TLBaseType" % (self.__class__, p[0]))
			self._params_map[p[0]] = p[1]
			pnames.append(p[0])
		return pnames

	def set_members(self, *args, **kw):
		"""
		Sets member value

		:param args: Unnamed member values that respect object structure order
		:param kw: Named member values
		:return:

		Example::

			class PersonType(TLCompositeType):
				def get_stucture(self):
					return ("name",TL_string("Unnamed")) ("age":TL_int(1))

			person= PersonType()
			person.set_members( "Chris", 20 )
			# next line has same effect as previous line
			person.set_members( age=20, name="Chris" )
			# ... as this
			person.set_members( "Chris", age=20)
		"""
		# assign first in unnamed order
		if len(args) > len(self._params_map):
			raise ValueError("count of member passed is > of current member count")
		for i in range(len(args)):
			name = self._params_ordered[i][0]
			self._params_map[name].set(args[i])
		for k in kw:
			self._params_map[k].set(kw[k])

	def get_structure(self):
		"""
		Describe the object structure. All subclass MUST override this abstract method if want members.

		:return: A tuple with ordered members description which follow the ( str(member_name), instance_of_TLBaseType_subclass ) format
		Example::

			# Person represent a person with a name and an age
			class Person(TLCompositeType):
				def get_structure(self):
					return ("name",TL_string("Unnamed")) ("age":TL_int(1))
		"""
		return None

	def to_dict(self):
		ret = {}
		for k in self._params_map:
			ret[k] = self._params_map[k]
		return ret

	def __setitem__(self, key, value):
		if not self._params_map.has_key(key):
			raise ValueError(key + " is not a valid member")
		self._params_map[key].set(value)

	def __getitem__(self, item):
		if not self._params_map.has_key(item):
			raise ValueError(item + " is not a valid member")
		return self._params_map[item].get()

	def __getattr__(self, item):
		if self._member_access_flag:
			if item in self._params_map:
				return self._params_map[item].get()
		return self.__getattribute__(item)


class TLConstructor(TLFunction):
	pass


def _uid(sid):
	if sid >= 0:
		return sid
	return 2 ** 32 + sid


class TLRegister(object):
	_func_map = {}  # func_id : func_class
	_abs_map = {}  # ctor_id: abs_class, ctor_class

	@classmethod
	def register(cls, *f):
		for tl in f:
			if issubclass(tl, TLConstructedType):
				cls.register_constructed_types(tl)
			elif issubclass(tl, TLFunction):
				cls.register_functions(tl)

	@classmethod
	def register_functions(cls, *f):
		for cf in f:
			if issubclass(cf, TLFunction):
				cls._func_map[cf.ID] = TLFunction

	@classmethod
	def register_constructed_types(cls, *ref_classes):
		for curr_class in ref_classes:
			if not issubclass(curr_class, TLConstructedType):
				continue
			if curr_class.CONSTRUCTORS_CLASSES is None:
				raise ValueError("AbstractType must be least a constructor")
			for ctor in curr_class.CONSTRUCTORS_CLASSES:
				cls._abs_map[ctor.ID] = (curr_class, ctor)

	@classmethod
	def get_abstract_type(cls, cid):
		cid = _uid(cid)
		return cls._abs_map[cid]

	@classmethod
	def get_func_type(cls, fid):
		fid = _uid(fid)
		if cls._func_map.has_key(fid):
			return cls._func_map[fid]
		if cls._abs_map.has_key(fid):
			return cls._abs_map[fid][1]
		return None

	@classmethod
	def get(cls, cid):
		cid = _uid(cid)
		if cls._func_map.has_key(cid):
			return cls._func_map[cid]
		if cls._abs_map.has_key(cid):
			return cls._abs_map[cid][1]
		return None


class TL_Ref(TLBaseType):
	def __init__(self, ref=None):
		super(TL_Ref, self).__init__(ref)

	def set(self, value):
		if value is not None and not isinstance(value, TLBaseType):
			raise Exception("Can only referrer to TLBaseType objects")
		super(TL_Ref, self).set(value)

	def _check_reference(self):
		if self.get() is None:
			raise Exception("Reference is None")

	def serialize(self):
		self._check_reference()
		return self.get().serialize()

	def deserialize_from(self, stream):
		self._check_reference()
		return self.get().deserialize(stream)

	def serialize_to(self, stream):
		self._check_reference()
		return self.get().serialize_to()
