#Testing connection to database
from Connection import *
CONNECTION = Connection();
CONNECTION.Impala(Daemon = '172.21.5.201')
print(CONNECTION.Execute("SHOW DATABASES"))
