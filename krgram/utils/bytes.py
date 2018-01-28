class Bytes(bytearray):

	@staticmethod
	def from_int( n, size=4, big_endian=True, signed=False ):
		if not signed and n <0: raise ValueError("if not signed n cannot be negative")
		if n<0:
			max_n_for_size = 2 ** (size * 8) - 1
			n= max_n_for_size+n+1
		curr_byte_i= 0
		ret= Bytes(size)
		while curr_byte_i < size:
			curr_byte= n & 0xff
			ret[ curr_byte_i if not big_endian else (size-1-curr_byte_i) ]= curr_byte
			n >>= 8
			curr_byte_i += 1
		return ret

	@staticmethod
	def flattern(seq):
		ret= Bytes()
		for i in seq:
			ret += i
		return ret

	def to_int(self, big_endian=True, signed=False):
		slen= len(self)
		r= range(slen)
		ret= 0
		for i in r:
			ret <<= 8
			ret += self[i if big_endian else slen-1-i]

		if signed:
			max_repr_for_size= 1<<(8*slen-1)
			if ret >= max_repr_for_size:
				ret= -2 * max_repr_for_size + ret
		return ret

	def __getitem__(self, item):
		if isinstance(item, slice):
			return Bytes(super(self.__class__, self).__getitem__(item))
		return super(self.__class__, self).__getitem__(item)

	def __xor__(self, other):
		int_xor= self.to_int() ^ other.to_int()
		return Bytes.from_int(int_xor, max(len(self), len(other)))

	def __repr__(self):
		s= ''
		c= 0
		ch= 0
		for i in self:
			if c == 0:
				s += "(%.4d)\t" % (ch*16)
				ch += 1
			elif c == 8:
				s += "  "
			s += "%.2x " % (i,)
			c += 1
			if (c % 16) == 0:
				s += "\n"
				c= 0
		return s+"\n"

	def __str__(self):
		r= ''
		for i in self:
			r += chr(i)
		return r

	def __bytes__(self):
		return self

	def to_hex_string(self):
		def niddle_to_char(n):
			if n < 10:
				return chr(n+48)
			return chr( 65 + n - 10)
		ret= ''
		for i in self:
			hniddle= (i & 0xf0)>>4
			lniddle= i & 0x0f
			ret += niddle_to_char(hniddle) + niddle_to_char(lniddle) + " "
		return ret


	def __add__(self, other):
		result = super(self.__class__, self).__add__(  other )
		return Bytes(result)



