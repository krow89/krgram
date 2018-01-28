class ClientError(Exception):
	pass

class SecurityError(ClientError):
	pass


class MTProtocolError(Exception):
	pass