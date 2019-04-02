#Testing connection to database
from Connection import *
CONNECTION = Connection();
CONNECTION.Impala(Daemon = '172.21.5.201')

MESSAGE = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.readings (id INT, mac STRING, pressure FLOAT, temperature FLOAT, humidity FLOAT)ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
#MESSAGE = "CREATE DATABASE IF NOT EXISTS dedomena COMMENT 'To store sensor reading' LOCATION '/test-warehouse/data/sensor';"
#MESSAGE = "CREATE DATABASE IF NOT EXISTS dedomena;"
MESSAGE = "DROP DATABASE dedomena;"
MESSAGE = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.readings (" \
          "id INT, " \
          "mac STRING, " \
          "pressure FLOAT, " \
          "temperature FLOAT, " \
          "humidity FLOAT)" \
          "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"

print(CONNECTION.Execute("SHOW DATABASES"))
CONNECTION.Execute(MESSAGE)

