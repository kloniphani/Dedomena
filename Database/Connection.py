class Connection(object):
	"""description of class"""
	
	CONNECTION =  None; 

	def Impala(self, Daemon, Port = 21050):
		from impala import dbapi;
		from sys import exc_info; 

		try:
			self.CONNECTION = dbapi.connect(Daemon, Port)
		except:
			print("Unexpected error: {0}".format(exc_info()[0]))

		return self.CONNECTION;

	def Hive(self, Server, Port = 10000):
		from pyhive import hive;
		from sys import exc_info;

		try:
			self.CONNECTION = hive.connect(Server, Port)
		except:
			print("Unexpected error: {0}".format(exc_info()[0]))
		
		return self.CONNECTION;

	def Execute(self, Query, Fetch = 'All'):
		from sys import exc_info;

		if self.CONNECTION is not None:
			try:
				cursor = self.CONNECTION.cursor()
				cursor.execute(Query)
				if(Fetch.lower() == 'all'):
					return cursor.fetchall()
				else:
					return cursor.fetchone()
			except:
				print("Unexpected error: {0}".format(exc_info()[0]))

		else:
			print("!Not connected to any database");													    
