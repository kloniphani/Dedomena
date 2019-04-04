from Connection import *



"""description of class"""
from sense_hat import SenseHat
import os, pyrebase, pubnub, sys, time, datetime;

def get_mac():
    import uuid
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    return mac

SENSE = SenseHat()
MacAddress = get_mac()

# Define the colours in a dictionary
COLOR = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'orange': (255, 165, 0),
    'yellow': (255, 225, 0),
    'cyan': (0, 255, 255),
    'violet': (238, 130, 238),
    'brown': (165, 42, 42),
    'purple': (128, 0, 128),
    'custom' : (255, 255, 255)
}


def connectToImpala(Daemon, Port = 21050):
    from time import sleep

    # Connecting to Impala database in Cloudera
    IMPALA_CONNECTION = Connection();
    IMPALA_CONNECTION.Impala(Daemon, Port)

    #Checking if the Database and Table exist
    Query = "CREATE DATABASE IF NOT EXISTS dedomena COMMENT 'Database to store sensor reading' LOCATION '/test-warehouse/data/sensor';"
    IMPALA_CONNECTION.Execute(Query)
    sleep(5)

    Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.sensor (" \
            "id_sensor int NOT NULL AUTO_INCREMENT" \
            "macAddress STRING, " \
            "manufacturer STRING, " \
            "model STRING," \
            "date STRING, " \
            "time STRING, " \
            "pressure FLOAT, " \
            "temperature FLOAT, " \
            "humidity FLOAT," \
            "magnetometer, FLOAT" \
            "x FLOAT, " \
            "y FLOAT, " \
            "z FLOAT, " \
            "pitch FLOAT, " \
            "roll FLOAT, " \
            "yaw FLOAT) " \
            "AUTO_INCREMENT=63 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci " \
            "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
    IMPALA_CONNECTION.Execute(Query)
    sleep(10)

    return IMPALA_CONNECTION



def pushSensorReadings(interval = 10, print_results = True):
    from time import sleep
    from datetime import datetime

    SERVER = '172.21.5.201'

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

            Acceleration = SENSE.get_accelerometer_raw()
            Orientation = SENSE.get_orientation()
            north = SENSE.get_compass()

            x = Acceleration['x']
            y = Acceleration['y']
            z = Acceleration['z']

            pitch = Orientation["pitch"]
            roll = Orientation["roll"]
            yaw = Orientation["yaw"]

            Query = "LOCK TABLES dedomena.sensor WRITE;" \
                    "INSERT INTO dedomena.sensor (macAddress, manufacturer, model, date, time, pressure, temperature, humidity, magnetometer, x, y, z, pitch, roll, yaw) " \
                    "VALUES({0}, {1}, {2}, {3});" \
                    "UNLOCK TABLES dedomena.sensor;".format(MacAddress, 'Raspberry Pi', 'Model B+', date_sense, time_sense, Pressure, Temperature, Humidity, north, x, y, z, pitch, roll, yaw)
            IMPALA_CONNECTION.Execute(Query)

            if print_results == True:
                print("Time: {0}\tMacAddress: {1}".format(time_sense, MacAddress))
                print("\tTemperature: {0}C\tPressure: {1}Mb\tHumidity: {2}%\n\n".format(Temperature, Pressure, Humidity))
                print("\tX={0}, Y={1}, Z={2}".format(x, y, z))
                print("\tPitch {0} Roll {1} Yaw {2}\n\n".format(pitch, roll, yaw))
        except Exception as e:
            raise
        sleep(interval)


def deviceState():
    while True:
        Acceleration = SENSE.get_accelerometer_raw()
        x = Acceleration['x']
        y = Acceleration['y']
        z = Acceleration['z']

        x = round(x, 0)
        y = round(y, 0)
        z = round(z, 0)

        if abs(x) > 1 or abs(y) > 1 or abs(z) > 1:
            # Update the rotation of the display depending on which way up the Sense HAT is
            if x == -1:
                SENSE.set_rotation(180)
            elif y == 1:
                SENSE.set_rotation(90)
            elif y == -1:
                SENSE.set_rotation(270)
            else:
                SENSE.set_rotation(0)

            SENSE.show_letter("!", COLOR['red'])
        else:
            SENSE.clear()


def joysticMovements():
    import time

    MessageSpeed = 0.05; ValueSpeed = 0.05
    TextColour = COLOR['orange'];
    while True:
        for event in SENSE.stick.get_events():
            # Check if the joystick was pressed
            if event.action == "pressed":

                # Check which direction
                if event.direction == "up":
                    SENSE.show_message("Temperature", text_colour=TextColour, scroll_speed=MessageSpeed)
                    SENSE.show_message("{0}C".format(round(SENSE.get_temperature(), 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
                elif event.direction == "down":
                    SENSE.show_message("Pressure", text_colour=TextColour, scroll_speed=MessageSpeed)
                    SENSE.show_message("{0}Mb".format(round(SENSE.get_pressure(), 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
                elif event.direction == "left":
                    SENSE.show_message("Humidity", text_colour=TextColour, scroll_speed=MessageSpeed)
                    SENSE.show_message("{0}%".format(round(SENSE.get_humidity(), 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
                elif event.direction == "right":
                    SENSE.show_message("Compass", text_colour=TextColour, scroll_speed=MessageSpeed)
                    SENSE.show_message("{0} N".format(round(SENSE.compass, 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
                elif event.direction == "middle":
                    SENSE.show_letter("!", text_colour=TextColour)

                # Wait a while and then clear the screen
                time.sleep(0.5)


if __name__ == '__main__':
    from multiprocessing import Process

    a = Process(target=joysticMovements)
    a.start()
    
    b = Process(target=deviceState)
    b.start()
    
    c = Process(target=pushSensorReadings)
    c.start()
    
    a.join()
    b.join()
    c.join

