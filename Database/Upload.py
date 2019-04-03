from Connection import *


class Upload(object):
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

    IMPALA_CONNECTION = None

    def connectToImpala(self, Daemon, Port = 21050):
        # Connecting to Impala database in Cloudera
        self.IMPALA_CONNECTION = Connection();
        self.IMPALA_CONNECTION.Impala(Daemon, Port)

    def pushEnvironmentalReadings(self, interval = 10, print_results = True):
        from time import sleep
        from datetime import datetime

        import sys

        #Take readings from all three sensors and ound the values to one decimal place
        while(True):
            try:
                Temperature = self.SENSE.get_temperature()
                Pressure = self.SENSE.get_pressure()
                Humidity = self.SENSE.get_humidity()

                time = datetime.now()
                time_sense = time.strftime('%H:%M:%S')
                date_sense = time.strftime('%d/%m/%Y')

                Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.device (" \
                        "macAddress STRING, " \
                        "manufacturer STRING, " \
                        "model STRING)" \
                        "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
                self.IMPALA_CONNECTION.Execute(Query)

                Query = "INSERT INTO dedomena.device (macAddress, manufacturer, model) VALUES({0}, {1}, {2});".format(self.MacAddress, 'Raspberry Pi', 'Model B');
                self.IMPALA_CONNECTION.Execute(Query)

                Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.timestamp (" \
                        "date STRING, " \
                        "time STRING) " \
                        "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
                #self.IMPALA_CONNECTION.Execute(Query)

                Query = "INSERT INTO dedomena.device (date, time) VALUES({0}, {1});".format(date_sense, time_sense);
                #self.IMPALA_CONNECTION.Execute(Query)

                Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.device (" \
                        "timestamp STRING, " \
                        "deviceMacAddress STRING, " \
                        "pressure FLOAT, " \
                        "temperature FLOAT, "\
                        "humidity FLOAT) " \
                        "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
                #self.IMPALA_CONNECTION.Execute(Query)

                Query = "INSERT INTO dedomena.device (timestamp,deviceMacAddress, pressure, temperature, humidity) VALUES(0, {0}, {1}, {2}, {3});".format(self.MacAddress, Pressure, Temperature, Humidity);
                #self.IMPALA_CONNECTION.Execute(Query)

                if print_results == True:
                    print("Time: {0}\tMacAddress: {1}".format(time_sense, self.MacAddress))
                    print("\tTemperature: {0}C\tPressure: {1}Mb\tHumidity: {2}%\n\n".format(Temperature, Pressure, Humidity))
            except Exception as e:
                raise
            sleep(interval)

    def pushMovementReadings(self, interval = 1, print_results = True):
        import time

        while(True):
            try:
                Acceleration = self.SENSE.get_accelerometer_raw()
                Orientation = self.SENSE.get_orientation()
                north = self.SENSE.get_compass()

                time_sense = self.time.strftime('%H:%M:%S')
                date_sense = self.time.strftime('%d/%m/%Y')
                data = {"MAC": self.MacAddress, "Date": date_sense, "Time": time_sense, "Acceleration": Acceleration, "Orientation": Orientation, "Compass": north}

                x = Acceleration['x']
                y = Acceleration['y']
                z = Acceleration['z']
                pitch = Orientation["pitch"]
                roll = Orientation["roll"]
                yaw = Orientation["yaw"]

                Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.acceleration (" \
                        "deviceMacAddress STRING, " \
                        "x FLOAT, " \
                        "y FLOAT, " \
                        "z FLOAT)" \
                        "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
                self.IMPALA_CONNECTION.Execute(Query)

                Query = "INSERT INTO `dedomena.acceleration` (`macAddress`, `manufacturer`, `model`) VALUES({0}, {1}, {2}, {3});".format(self.MacAddress, x, y, z);
                self.IMPALA_CONNECTION.Execute(Query)

                Query = "CREATE EXTERNAL TABLE IF NOT EXISTS dedomena.orientation (" \
                        "deviceMacAddress STRING, " \
                        "pitch FLOAT, " \
                        "roll FLOAT, " \
                        "yaw FLOAT) " \
                        "ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION '/test-warehouse/data/sensor';"
                self.IMPALA_CONNECTION.Execute(Query)

                Query = "INSERT INTO `dedomena.orientation` (`macAddress`, `manufacturer`, `model`) VALUES({0}, {1}, {2}, {3});".format(self.MacAddress, pitch, roll, yaw);
                self.IMPALA_CONNECTION.Execute(Query)

                if print_results == True:
                    print("Time: {0}\tMacAddress: {1}".format(time_sense, self.MacAddress))
                    print("\tX={0}, Y={1}, Z={2}".format(x, y, z))
                    print("\tPitch {0} Roll {1} Yaw {2}\n\n".format(pitch, roll, yaw))
            except Exception as e:
                raise
            time.sleep(interval)

    def deviceState(self):
        while True:
            Acceleration = self.SENSE.get_accelerometer_raw()
            x = Acceleration['x']
            y = Acceleration['y']
            z = Acceleration['z']

            x = round(x, 0)
            y = round(y, 0)
            z = round(z, 0)

            if abs(x) > 1 or abs(y) > 1 or abs(z) > 1:
                # Update the rotation of the display depending on which way up the Sense HAT is
                if x == -1:
                    self.SENSE.set_rotation(180)
                elif y == 1:
                    self.SENSE.set_rotation(90)
                elif y == -1:
                    self.SENSE.set_rotation(270)
                else:
                    self.SENSE.set_rotation(0)

                SENSE.show_letter("!", self.COLOR['red'])
            else:
                self.SENSE.clear()

    def joysticMovements(self):
        import time

        MessageSpeed = 0.05; ValueSpeed = 0.05
        TextColour = self.COLOR['orange'];
        while True:
            for event in self.SENSE.stick.get_events():
                # Check if the joystick was pressed
                if event.action == "pressed":

                    # Check which direction
                    if event.direction == "up":
                        self.SENSE.show_message("Temperature", text_colour=TextColour, scroll_speed=MessageSpeed)
                        self.SENSE.show_message("{0}C".format(round(self.SENSE.get_temperature(), 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
                    elif event.direction == "down":
                        self.SENSE.show_message("Pressure", text_colour=TextColour, scroll_speed=MessageSpeed)
                        self.SENSE.show_message("{0}Mb".format(round(self.SENSE.get_pressure(), 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
                    elif event.direction == "left":
                        self.SENSE.show_message("Humidity", text_colour=TextColour, scroll_speed=MessageSpeed)
                        self.SENSE.show_message("{0}%".format(round(self.SENSE.get_humidity(), 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
                    elif event.direction == "right":
                        self.SENSE.show_message("Compass", text_colour=TextColour, scroll_speed=MessageSpeed)
                        self.SENSE.show_message("{0} N".format(round(self.SENSE.compass, 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
                    elif event.direction == "middle":
                        self.SENSE.show_letter("!", text_colour=TextColour)

                    # Wait a while and then clear the screen
                    time.sleep(0.5)


if __name__ == '__main__':
    from multiprocessing import Process

    uploadToImpala = Upload()
    uploadToImpala.connectToImpala('172.21.5.201', 21050)
    uploadToImpala.pushEnvironmentalReadings()

    """a = Process(target=uploadToImpala.joysticMovements)
    a.start()
    
    b = Process(target=uploadToImpala.deviceState)
    b.start()
    
    c = Process(target=uploadToImpala.pushEnvironmentalReadings)
    c.start()
    
    d = Process(target=uploadToImpala.pushMovementReadings)
    d.start()
    
    a.join()
    b.join()
    c.join()
    d.join"""

