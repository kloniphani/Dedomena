def checkDatabase(Server):
    from time import sleep

    IMPALA_CONNECTION = connectToImpala(Server)

    # Checking the Tables and Database in the server
    Query = "CREATE DATABASE IF NOT EXISTS dedomena COMMENT 'Database to store sensor reading' LOCATION '/test-warehouse/data/sensor';"
    IMPALA_CONNECTION.Execute(Query)

    Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.sensor (" \
            "id_sensor int NOT NULL AUTO_INCREMENT" \
            "macAddress STRING, " \
            "pressure FLOAT, " \
            "temperature FLOAT, " \
            "humidity FLOAT," \
            "magnetometer, FLOAT" \
            "timestamp INT, " \
            "acceleration INT," \
            "gyroscope INT," \
            "PRIMARY KEY (id_sensor), " \
            "KEY sensorTimestamp (timestamp), " \
            "KEY sensorDevice (macAddress), " \
            "KEY sensorAcceleration (acceleration), " \
            "KEY sensorGyroscope (gyroscope), " \
            "CONSTRAINT sensorTimestamp FOREIGN KEY (timestamp) REFERENCES dedomena.timestamp (id_timestamp), " \
            "CONSTRAINT sensorDevice FOREIGN KEY (macAddress) REFERENCES dedomena.device  (id_device ), " \
            "CONSTRAINT sensorAcceleration FOREIGN KEY (acceleration) REFERENCES dedomena.acceleration (id_acceleration), " \
            "CONSTRAINT sensorGyroscope FOREIGN KEY (gyroscope) REFERENCES dedomena.gyroscope (id_gyroscope)) " \
            "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
    IMPALA_CONNECTION.Execute(Query)

    Query = "CREATE DATABASE IF NOT EXISTS dedomena COMMENT 'Database to store sensor reading' LOCATION '/test-warehouse/data/sensor';"
    IMPALA_CONNECTION.Execute(Query)

    Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.device (" \
            "id_device int NOT NULL AUTO_INCREMENT" \
            "macAddress STRING, " \
            "manufacturer STRING, " \
            "model STRING," \
            "firmware STRING, " \
            "platform STRING, " \
            "PRIMARY KEY (id_device, macAddress))" \
            "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
    IMPALA_CONNECTION.Execute(Query)

    Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.timestamp (" \
            "id_timestamp int NOT NULL AUTO_INCREMENT" \
            "stamp STRING, " \
            "date STRING, " \
            "time STRING, " \
            "zone STRING, " \
            "PRIMARY KEY (timestamp)) " \
            "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
    IMPALA_CONNECTION.Execute(Query)

    Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.acceleration (" \
            "id_acceleration int NOT NULL AUTO_INCREMENT" \
            "x FLOAT, " \
            "y FLOAT, " \
            "z FLOAT" \
            "PRIMARY KEY (id_acceleration))" \
            "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
    IMPALA_CONNECTION.Execute(Query)

    Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.gyroscope (" \
            "id_gyroscope int NOT NULL AUTO_INCREMENT" \
            "pitch FLOAT, " \
            "roll FLOAT, " \
            "yaw FLOAT" \
            "PRIMARY KEY (id_orientation)) " \
            "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
    IMPALA_CONNECTION.Execute(Query)
    sleep(10)


def pushSensorReadings(interval = 10, print_results = True):
    from time import sleep
    from datetime import datetime

    SERVER = '172.21.5.201'
    checkDatabase(SERVER)

    #Take readings from all three sensors and ound the values to one decimal place
    IMPALA_CONNECTION = connectToImpala(SERVER)
    while(True):
        try:
            Temperature = SENSE.get_temperature()
            Pressure = SENSE.get_pressure()
            Humidity = SENSE.get_humidity()

            time = datetime.now()
            time_sense = time.strftime('%H:%M:%S')
            date_sense = time.strftime('%d/%m/%Y')
            stamp = date_sense + ' ' + time_sense

            Acceleration = SENSE.get_accelerometer_raw()
            Orientation = SENSE.get_orientation()
            north = SENSE.get_compass()

            x = Acceleration['x']
            y = Acceleration['y']
            z = Acceleration['z']

            pitch = Orientation["pitch"]
            roll = Orientation["roll"]
            yaw = Orientation["yaw"]

            Query = "LOCK TABLES dedomena.device WRITE;" \
                    "INSERT INTO dedomena.device (macAddress, manufacturer, model) " \
                    "VALUES('{0}', '{1}', '{2}');" \
                    "UNLOCK TABLES dedomena.device;".format(MacAddress, 'Raspberry Pi', 'Model B+')
            IMPALA_CONNECTION.Execute(Query)

            Query = "LOCK TABLES dedomena.timestamp WRITE;" \
                    "INSERT INTO dedomena.timestamp (date, time) " \
                    "VALUES({0}, {1});" \
                    "UNLOCK TABLES dedomena.timestamp;".format(date_sense, time_sense)
            IMPALA_CONNECTION.Execute(Query)

            Query = "LOCK TABLES dedomena.acceleration WRITE;" \
                    "INSERT INTO dedomena.acceleration (x, y, z) " \
                    "VALUES({0}, {1}, {2};" \
                    "UNLOCK TABLES dedomena.acceleration;".format(x, y, z)
            IMPALA_CONNECTION.Execute(Query)

            Query = "LOCK TABLES dedomena.gyroscope WRITE;" \
                    "INSERT INTO dedomena.gyroscope (pitch, roll, yaw) " \
                    "VALUES({0}, {1}, {2});" \
                    "UNLOCK TABLES dedomena.gyroscope;".format(pitch, roll, yaw)
            IMPALA_CONNECTION.Execute(Query)

            Query = "LOCK TABLES dedomena.sensor WRITE;" \
                    "INSERT INTO dedomena.sensor (pressure, temperature, humidity, magnetometer) " \
                    "VALUES({0}, {1}, {2}, {3});" \
                    "UNLOCK TABLES dedomena.sensor;".format(Pressure, Temperature, Humidity, north)
            IMPALA_CONNECTION.Execute(Query)

            if print_results == True:
                print("Time: {0}\tMacAddress: {1}".format(time_sense, MacAddress))
                print("\tTemperature: {0}C\tPressure: {1}Mb\tHumidity: {2}%\n\n".format(Temperature, Pressure, Humidity))
                print("\tX={0}, Y={1}, Z={2}".format(x, y, z))
                print("\tPitch {0} Roll {1} Yaw {2}\n\n".format(pitch, roll, yaw))
        except Exception as e:
            raise
        sleep(interval)

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

