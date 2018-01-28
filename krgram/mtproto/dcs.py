_default_dcs = (
	(1, "149.154.175.50", "149.154.175.10"),
	(2, "149.154.167.51", "149.154.167.40"),
	(3, "149.154.175.100", "149.154.175.117"),
	(121, "95.213.217.195", "95.213.217.195")
)


class DataCenter:

	def __init__(self, dcid, prod_ip, test_ip):
		self.id = dcid
		self.production_ip = prod_ip
		self.test_ip = test_ip


class DataCenters:
	_default = None

	def __init__(self):
		self._datacenters = {}

	def set_datacenter(self, dcid, production_ip, test_ip):
		self._datacenters[dcid] = DataCenter(dcid, production_ip, test_ip)

	def get_datacenter(self, dcid):
		if dcid in self._datacenters:
			return self._datacenters[dcid]
		return None

	@staticmethod
	def get_default():
		cls = DataCenters
		if cls._default is None:
			cls._default = DataCenters()
			for dc in _default_dcs:
				cls._default.set_datacenter(dc[0], dc[1], dc[2])
		return cls._default
