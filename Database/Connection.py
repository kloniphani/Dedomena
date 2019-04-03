class Connection(object):
	"""description of class"""
	
	CONNECTION =  None; 

	def Impala(self, Daemon, Port = 21050):
		from impala import dbapi;
		from sys import exc_info; 

		try:
			self.CONNECTION = dbapi.connect(Daemon, Port)
		except:
			print("Unexpected error on function: {0}\nClass:\t{1]\nDetails:\t{2}".format("Impala", exc_info()[0], exc_info()[1]))

		return self.CONNECTION;

	def Hive(self, Server, Port = 10000):
		from pyhive import hive;
		from sys import exc_info;

		try:
			self.CONNECTION = hive.connect(Server, Port)
		except:
			print("Unexpected error on function: {0}\nClass:\t{1]\nDetails:\t{2}".format("Hive", exc_info()[0], exc_info()[1]))
		
		return self.CONNECTION;

	def Execute(self, Query, Fetch = 'All'):
		from sys import exc_info;

		if self.CONNECTION is not None:
			try:
				cursor = self.CONNECTION.cursor()
				cursor.execute(Query)
				if(Fetch.lower() == 'all' and cursor != None):
					return cursor.fetchall()
				else:
					return cursor.fetchone()
			except:
				print("Unexpected error on function: {0}\nClass:\t{1]\nDetails:\t{2}".format("Excute",exc_info()[0],exc_info()[1]))
		else:
			print("!Not connected to any database")
		return None
