class Connection(object):
	"""description of class"""

	CONNECTION =  None; 

	def Impala(self, Daemon, Port = 21050):
		from impala import dbapi;
		CONNECTION = dbapi.connect(Deamon, Port)

	def Hive(self, Server, Port = 10000):
		from pyhive import hive;
		CONNECTION = hive.connect(Server, Port)

	def Execute(self, Query, Fetch = 'All'):
		if CONNECTION is not None:
			cursor = CONNECTION.cursor()
			cursor.execute(Query)
			if(Fetch.lower() == 'all'):
				return cursor.fetchall()
			else:
				return cursor.fetchone()
		else:
			print: "!Not connected to any database";
