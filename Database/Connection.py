class Connection(object):
	"""description of class"""

	CONNECTION =  None; 

	def Impala(self, Daemon, Port = 21050):
		from impala import dbapi;
		self.CONNECTION = dbapi.connect(Daemon, Port)

	def Hive(self, Server, Port = 10000):
		from pyhive import hive;
		self.CONNECTION = hive.connect(Server, Port)

	def Execute(self, Query, Fetch = 'All'):
		if self.CONNECTION is not None:
			cursor = self.CONNECTION.cursor()
			cursor.execute(Query)
			if(Fetch.lower() == 'all'):
				return cursor.fetchall()
			else:
				return cursor.fetchone()
		else:
			print("!Not connected to any database");
