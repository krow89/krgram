from krgram.tl.base import TLConstructor, TLConstructedType, TLFunction, TLRegister
from krgram.tl.core_types import TL_int_as_string, TL_int128, TL_int256, TL_string, TL_long, TL_int, Vector, vector


#
# ResPQ
#
class req_pq(TLFunction):
	ID = 0x60469778

	def get_structure(self):
		return "nonce", TL_int128(0)


class resPQ(TLConstructor):
	ID = 0x05162463

	def get_structure(self):
		return ("nonce", TL_int128(0)), \
			   ("server_nonce", TL_int128(0)), \
			   ("pq", TL_int_as_string(size=8)), \
			   ("server_public_key_fingerprints", Vector(vector(lambda: TL_long())))


class ResPQ(TLConstructedType):
	CONSTRUCTORS_CLASSES = (resPQ,)


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


class Server_DH_Params(TLConstructedType):
	CONSTRUCTORS_CLASSES = (server_DH_params_ok,
							server_DH_params_fail)


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


#
# Client_DH_Inner_Data
#
class client_DH_inner_data(TLConstructor):
	ID = 0x6643b654

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("retry", TL_long()), (
			"g_b", TL_int_as_string(size=256))


class Client_DH_Inner_Data(TLConstructedType):
	CONSTRUCTORS_CLASSES = (client_DH_inner_data,)


#
# Set_client_DH_params_answer
#
class set_client_DH_params(TLFunction):
	ID = 0xf5045f1f

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("encrypted_data", TL_string())


class dh_gen_ok(TLConstructor):
	ID = 0x3bcbf734

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("new_nonce_hash1", TL_int128())


class dh_gen_retry(TLConstructor):
	ID = 0x46dc1fb9

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("new_nonce_hash2", TL_int128())


class dh_gen_fail(TLConstructor):
	ID = 0xa69dae02

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("new_nonce_hash3", TL_int128())


class Set_client_DH_params_answer(TLConstructedType):
	CONSTRUCTORS_CLASSES = (dh_gen_ok, dh_gen_fail, dh_gen_fail)


#
# DestroyAuthKeyRes
#
class destroy_auth_key(TLFunction):
	ID = 0xd1435160


class destroy_auth_key_ok(TLConstructor):
	ID = 0xf660e1d4


class destroy_auth_key_none(TLConstructor):
	ID = 0x0a9f2259


class destroy_auth_key_fail(TLConstructor):
	ID = 0xea109b13


class DestroyAuthKeyRes(TLConstructedType):
	CONSTRUCTORS_CLASSES = destroy_auth_key_ok, \
						   destroy_auth_key_none, \
						   destroy_auth_key_fail

#
#
#
class req_DH_params(TLFunction):
	ID = 0xd712e4be

	def get_structure(self):
		return ("nonce", TL_int128()), ("server_nonce", TL_int128()), ("p", TL_int_as_string(size=4)), (
			"q", TL_int_as_string(size=4)), \
			   ("public_key_fingerprint", TL_long()), ("encrypted_data", TL_string())


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


class ping(TLFunction):
	ID = 0x7abe77ec

	def get_structure(self):
		return "ping_id", TL_long()


# Constructed Types
TLRegister.register(P_Q_inner_data,
					Server_DH_Params,
					Server_DH_inner_data,
					Client_DH_Inner_Data,
					Set_client_DH_params_answer,
					ResPQ,
					RpcDropAnswer)


# Functions
TLRegister.register(req_DH_params,
					set_client_DH_params,
					req_pq,
					destroy_auth_key)
