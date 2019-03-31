#Testing connection to database
from Connection import *
CONNECTION = Connection();
CONNECTION.Hive(Server = '172.21.5.201')
print(CONNECTION.Execute("SHOW DATABASES"))
