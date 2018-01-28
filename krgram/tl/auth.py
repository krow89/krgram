from krgram.tl.types import *


class TL_int128(TL_int):
	def __init__(self, v=0):
		super(TL_int128, self).__init__(v, signed=False)

	def serialize(self):
		v = self.get()
		return Bytes.from_int(v, 16, True)

	def deserialize_from(self, stream):
		self.set(Bytes(stream.read(16)).to_int(True))
		return self


class TL_int256(TL_int):
	def serialize(self):
		return Bytes.from_int(self.get(), 32, True, signed=self._signed)

	def deserialize_from(self, stream):
		self.set(Bytes(stream.read(32)).to_int(True))
		return self


class TL_int_as_string(TL_int):
	def __init__(self, i=0, size=4, signed=False):
		super(TL_int_as_string, self).__init__(i, signed=signed)
		self._byte_len = size

	def serialize(self):
		itos = Bytes.from_int(self.get(), self._byte_len, True, self._signed)
		tls = TL_string(itos)
		return tls.serialize()

	def deserialize_from(self, stream):
		tls = TL_string()
		tls.deserialize_from(stream)
		self.set(Bytes(tls.get()).to_int(True, self._signed))
		return self


#
# P_Q_inner_data
#
class p_q_inner_data(TLConstructor):
	ID = 0x83c95aec

	def get_structure(self):
		return ("pq", TL_int_as_string(size=8)), \
			   ("p", TL_int_as_string(size=4)), \
			   ("q", TL_int_as_string(size=4)), \
			   ("nonce", TL_int128(0)), \
			   ("server_nonce", TL_int128(0)), \
			   ("new_nonce", TL_int256())


class P_Q_inner_data(TLConstructedType):
	CONSTRUCTORS_CLASSES = (p_q_inner_data,)


TLRegister.register_constructed_types(P_Q_inner_data)


#
# Server_DH_Params
#
class server_DH_params_ok(TLConstructor):
	ID = 0xd0e8075c

	def get_structure(self):
		return ("nonce", TL_int128(0)), ("server_nonce", TL_int128(0)), ("encrypted_answer", TL_string())


class server_DH_params_fail(TLConstructor):
	ID = 0x79cb045d

	def get_structure(self):
		return ("nonce", TL_int128(0)), ("server_nonce", TL_int128(0)), ("new_nonce_hash", TL_int128())


class req_DH_params(TLFunction):
	ID = 0xd712e4be

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("p", TL_int_as_string(size=4)), (
		"q", TL_int_as_string(size=4)), \
			   ("public_key_fingerprint", TL_long()), ("encrypted_data", TL_string())


class Server_DH_Params(TLConstructedType):
	CONSTRUCTORS_CLASSES = (server_DH_params_ok,
							server_DH_params_fail)


TLRegister.register_constructed_types(Server_DH_Params)
TLRegister.register_functions(req_DH_params)


#
# Server_DH_inner_data
#
class server_DH_inner_data(TLConstructor):
	ID = 0xb5890dba

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("g", TL_int()), (
		"dh_prime", TL_int_as_string(size=256)), \
			   ("g_a", TL_int_as_string(size=256)), ("server_time", TL_int(signed=False))


class Server_DH_inner_data(TLConstructedType):
	CONSTRUCTORS_CLASSES = (server_DH_inner_data,)


TLRegister.register_constructed_types(Server_DH_inner_data)


#
# Client_DH_Inner_Data
#
class set_client_DH_params(TLFunction):
	ID = 0xf5045f1f

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("encrypted_data", TL_string())


class client_DH_inner_data(TLConstructor):
	ID = 0x6643b654

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("retry", TL_long()), (
		"g_b", TL_int_as_string(size=256))


class Client_DH_Inner_Data(TLConstructedType):
	CONSTRUCTORS_CLASSES = (client_DH_inner_data,)


TLRegister.register_constructed_types(Client_DH_Inner_Data)
TLRegister.register_functions(set_client_DH_params)


#
# Set_client_DH_params_answer
#
class dh_gen_ok(TLFunction):
	ID = 0x3bcbf734

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("new_nonce_hash1", TL_int128())


class dh_gen_retry(TLFunction):
	ID = 0x46dc1fb9

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("new_nonce_hash2", TL_int128())


class dh_gen_fail(TLFunction):
	ID = 0xa69dae02

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("new_nonce_hash3", TL_int128())


class Set_client_DH_params_answer(TLConstructedType):
	CONSTRUCTORS_CLASSES = (dh_gen_ok, dh_gen_fail, dh_gen_fail)


TLRegister.register_constructed_types(Set_client_DH_params_answer)


#
# ResPQ
#
class resPQ(TLConstructor):
	ID = 0x05162463

	def get_structure(self):
		return ("nonce", TL_int128(0)), \
			   ("server_nonce", TL_int128(0)), \
			   ("pq", TL_int_as_string(size=8)), \
			   ("server_public_key_fingerprints", Vector(vector(lambda: TL_long())))


class req_pq(TLFunction):
	ID = 0x60469778

	def get_structure(self):
		return "nonce", TL_int128(0)


class ResPQ(TLConstructedType):
	CONSTRUCTORS_CLASSES = (resPQ,)


TLRegister.register_constructed_types(ResPQ)
TLRegister.register_functions(req_pq)


#
# RpcDropAnswer
#
class rpc_answer_unknown(TLConstructor):
	ID = 0x5e2ad36e


class rpc_answer_dropped_running(TLConstructor):
	ID = 0xcd78e586


class rpc_answer_dropped(TLConstructor):
	ID = 0xa43ad8b7

	def get_structure(self):
		return ("msg_id", TL_long(0)), ("seq_no", TL_int(0)), ("bytes", TL_int(None))


class RpcDropAnswer(TLConstructedType):
	CONSTRUCTORS_CLASSES = (rpc_answer_unknown,
							rpc_answer_dropped_running,
							rpc_answer_dropped)


TLRegister.register_constructed_types(Set_client_DH_params_answer)
TLRegister.register_functions(req_pq)


class ping(TLFunction):
	ID = 0x7abe77ec

	def get_structure(self):
		return "ping_id", TL_long()
