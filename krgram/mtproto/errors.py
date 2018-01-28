class MTProtoError(Exception):
	pass


class MTProtoFatalError(MTProtoError):
	"""
	An error in protocol implementation
	"""
	pass


class UnexpectedResponseError(MTProtoError):
	"""
	An unexpected response receveid from server
	"""
	pass


class UnexpectedResponseIdError(UnexpectedResponseError):
	def __init__(self, unexpected_id):
		self._id = unexpected_id

	def __str__(self):
		return "%s: unexpected id= %x" % (self.__class__, self._id)
