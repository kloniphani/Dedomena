class Connection(object):
    """description of class"""

    CONNECTION =  None;

    def Impala(self, Daemon, Port = 21050):
        from impala import dbapi;
        from sys import exc_info;

        try:
            self.CONNECTION = dbapi.connect(Daemon, Port)
            print("+Successfully connected to: {0} with port: {1}\n\n".format(Daemon, Port))
        except Exception as e:
            print("Unexpected error on function: {0}\nDetails:\t{1}".format("Impala", e))

        return self.CONNECTION;

    def Hive(self, Server, Port = 10000):
        from pyhive import hive;
        from sys import exc_info;

        try:
            self.CONNECTION = hive.connect(Server, Port)
            print("+Successfully connected to: {0} with port: {1}\n\n".format(Server, Port))
        except Exception as e:
            print("Unexpected error on function: {0}\nDetails:\t{1}".format("Hive", e))

        return self.CONNECTION;

    def Execute(self, Query, Fetch = 'none'):
        from sys import exc_info;

        if self.CONNECTION is not None:
            try:
                cursor = self.CONNECTION.cursor()
                cursor.execute(Query)

                if(Fetch.lower() == 'none'):
                    return None
                elif(Fetch.lower() == 'all' and cursor != None):
                    return cursor.fetchall()
                else:
                    return cursor.fetchone()
            except Exception as e:
                print("Unexpected error on function: {0}\nDetails:\t{1}".format("Excute", e))
            finally:
                cursor.close()
        else:
            print("!Not connected to any database")
        return None
