#
# TL classes generator (not-ready)
#

import re


class TLEntity(object):
	def __init__(self, name, ns):
		self._name = name
		self._ns = ns
		self._id = name if ns is None else ns+"."+name

	def get_name(self): return self._name
	def get_namespace(self): return self._ns
	def get_id(self): return self._id

class TLparam(object):
	def __init__(self, name, type):
		self._name = name
		self._type = type

	def get_name(self): return self._name
	def get_type(self): return self._type

class BaseExpression(object):
	def __init__(self, full_name):
		self.full_name = full_name
		p = full_name.split(".")
		if len(p) > 2:
			raise Exception("Unexpected name format ( different from [namespace.]name )")
		self.namespace = p[0] if len(p) > 1 else None
		self.name = p[1] if len(p) > 1 else full_name

class StructExpression(BaseException):
	def __init__(self, full_name, params):
		super(StructExpression, self).__init__(full_name)
		self.params = params

class FunctionExpression(StructExpression):
	def __init__(self, full_name, func_id, params, return_type):
		super(FunctionExpression, self).__init__(full_name, params)
		self._id = func_id
		self._ret_type = return_type

class CtorExpression(FunctionExpression):
	pass


class TLExpression:
	CTOR_DEF = 1
	FUNC_DEF = 2
	def __init__(self, full_name, definition):
		pass


class TLFunc(TLEntity):
	def __init__(self, name, ns, func_id, params, return_type):
		assert isinstance(name, str) and isinstance(return_type, TLEntity)
		super(TLFunc, self).__init__(name, ns)
		self._tl_id = func_id
		self._params = params
		self._ret_type = return_type

	def get_tl_id(self): return self._tl_id
	def get_params(self): return self._params
	def get_return_type(self): return self._ret_type

class SingleInstanceCreator:
	def __init__(self):
		self._pool = {}

	def get_instance(self, id, creator):
		if id not in self._pool:
			self._pool[id] = creator()
		return self._pool[id]



class TLEntities:
	def __init__(self):
		self._ns_register = {}
		self._g_register = {}
		self._init_module(self._g_register)


	def _init_module(self, container, sub=None):
		if sub is not None:
			if sub not in container:
				container[sub] = {}
			container = container[sub]
		if "types" not in container:
			container["types"] = {}
			container["functions"] = {}
		return container

	def get_entity(self, name, ns=None):
		if ns is None:
			register = self._g_register
		else:
			register = self._init_module(self._ns_register, ns)
		if not name in register:
			register[name] = TLEntities()
		return register[name]


class TLFunction:
	def __init__(self, fid, params, return_type):
		pass


class TLFileParser:
	_LINE_REGEXPR = re.compile(r'([a-zA-Z0-9_\.]+)(#([0-9a-fA-F]{1,8}))?(( \S+:\S+)*)? = ([a-zA-Z0-9_\.]+);?')#((A-Z)[a-zA-Z0-9_]*);')#(#9299359f) max_delay:int wait_after:int max_wait:int = HttpWait')
	_CTX_TYPE_DEFS_LINE = "---types---"
	_CTX_FUNCTION_DEFS_LINE = "---functions---"
	_CTX_TYPE_DEFS = 0
	_CTX_FUNCTION_DEFS = 1

	# some types (native) have direct relation with krgram types
	# they are declared as TL_* where * is native tl type (example int -> TL_int)
	_NATIVE_TYPES = ("int", "long", "byte", "string", "int128", "int256", "double")

	# other types have indirect relation with corrispective krgram types (eg. are declare with different names)
	_COERCIABLE_TYPES = ("vector", "Vector", "#", "Type", "!#")



	def __init__(self, path):
		self._fpath = path
		self._bad_lines = None
		self._ctors = None
		self._funcs = None
		self._structs = None

	def _parse_native_type(self, type_str):
		if type_str in self._NATIVE_TYPES:
			return "TL_" + type_str
		return None

	def parse(self): # --> TLEntitities
		tl_file = open(self._fpath, "r")

		# reset internal data
		self._bad_lines = []
		self._ctors = []
		self._funcs = []
		self._structs = []

		# default cotnext is type definitions
		curr_ctx = self._CTX_TYPE_DEFS
		curr_line = tl_file.readline()
		expr_pattern = self._LINE_REGEXPR
		line_index = 1
		while curr_line != "":

			is_expr_line = True
			curr_line = curr_line[:-1] # leave final "\n" (TODO: leave it in os-indipendent way)

			# line with single char is unparsable
			if len(curr_line) == 1:
				tl_file.close()
				raise Exception("Invalid line at index %d " %(line_index))

			# handle empty and comment line
			elif len(curr_line)==0 or curr_line[:2]=="//":
				is_expr_line = False

			# handle change context line
			elif curr_line == self._CTX_FUNCTION_DEFS_LINE:
				curr_ctx = self._CTX_FUNCTION_DEFS
				is_expr_line = False
			elif curr_line == self._CTX_TYPE_DEFS_LINE:
				curr_ctx = self._CTX_TYPE_DEFS
				is_expr_line = False

			if is_expr_line:
				matcher = expr_pattern.match(curr_line)
				if matcher is None:
					self._bad_lines.append(curr_line)
				else:
					full_name = matcher.group(1)
					tl_id = matcher.group(3)
					params_str = matcher.group(4)
					ret_type = matcher.group(6)
					params_parsed = None
					if params_str != '':
						params_parsed = []
						params_str = params_str.strip()
						params = params_str.split(" ")
						for p in params:
							pname, ptype = p.split(":")
							params_parsed.append( (pname, ptype) )

					if tl_id is None:
						self._structs.append( StructExpression(full_name, params_parsed) )
					elif curr_ctx == self._CTX_TYPE_DEFS:
						self._ctors.append( CtorExpression(full_name, tl_id, params_parsed, ret_type) )
					else: # _CTX_FUNCTION_DEFS
						self._funcs.append( FunctionExpression(full_name, tl_id, params_parsed, ret_type) )

			curr_line = tl_file.readline()
			line_index += 1
		tl_file.close()
		return self


system_tl = TLFileParser("system.tl").parse()
auth_tl = TLFileParser("system.tl").parse()
api_tl = TLFileParser("api.tl").parse()

dummy  = 0

