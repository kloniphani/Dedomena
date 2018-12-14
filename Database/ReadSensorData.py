from sense_hat import SenseHat
from time import sleep, time
from multiprocessing import Process
from pubnub.pubnub import PubNub, SubscribeListener, SubscribeCallback, PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.exceptions import PubNubException

import uuid, os, pyrebase, pubnub, sys, time, datetime;
import mysql.connector

def get_mac():
  mac_num = hex(uuid.getnode()).replace('0x', '').upper()
  mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
  return mac

sense = SenseHat()
MacAddress = get_mac()
channel='senseHat'                         # provide pubnub channel_name



# Define the colours in a dictionary
COLOR = {
    'red' : (255, 0, 0),
    'green': (0, 255, 0),
    'blue' : (0, 0, 255),
    'black' : (0, 0, 0),
    'white' : (255, 255, 255),
    'orange': (255, 165, 0),
    'yellow' : (255, 225, 0),
    'cyan' : (0, 255, 255),
    'violet' : (238, 130, 238),
    'brown' : (165, 42, 42),
    'purple' : (128, 0, 128),
}

Config = {
    "apiKey": "AIzaSyCYu7gE_4HGDIy7pOOiw0AY-rrUmoE7eXQ",
    "authDomain": "sensehat-51bd7.firebaseapp.com",
    "databaseURL": "https://sensehat-51bd7.firebaseio.com",
    "storageBucket": "sensehat-51bd7.appspot.com"
}

Firebase = pyrebase.initialize_app(Config)
db = Firebase.database()

pnconf = PNConfiguration(); sleep(2)


pnconf.publish_key = 'pub-c-23235607-897e-4e8c-8b96-409d2a0ce710'       # set pubnub publish_key
pnconf.subscribe_key = 'sub-c-7b8840c4-f940-11e8-ba8a-aef4d14eb57e'     # set pubnub subscibe_key

pubnub = PubNub(pnconf)                     # create pubnub_object using pubnub_configuration_object

def my_publish_callback(envelope, status):
    if not status.is_error():
        pass
    else:
        pass


my_listener = SubscribeListener()                   # create listner_object to read the msg from the Broker/Server
pubnub.add_listener(my_listener)                    # add listner_object to pubnub_object to subscribe it
pubnub.subscribe().channels(channel).execute()      # subscribe the channel (Runs in background)


my_listener.wait_for_connect()                      # wait for the listner_obj to connect to the Broker.Channel
print('Connected to PubNub')                        # print confirmation msg

#Connection to MySQL
cnx = mysql.connector.connect(user='adam', password='passwd',
                              host='10.48.80.33',
                              port='3306',
                              database='dedomena')
try:
    cursor = cnx.cursor();
    cursor.execute("show tables;");
    result = cursor.fetchall();
    print("%Successfully Connected to the database with these tables -- {0}".format(result));
except:
    cnx.rollback()
    print('!Could not connect to MySql\n\tError: {0}'.format(sys.exc_info()[0]));


def pushEnvironmentalReadings(interval = 10, print_results = True):
    #Take readings from all three sensors and ound the values to one decimal place
    while(True):
        try:
            Temperature = sense.get_temperature()
            Pressure = sense.get_pressure()
            Humidity = sense.get_humidity()

            time_sense = time.strftime('%H:%M:%S')
            date_sense = time.strftime('%d/%m/%Y')
            data = {"MAC": MacAddress, "Date": date_sense, "Time": time_sense, "Temperature": Temperature, "Humidity": Humidity, "Pressure": Pressure}

            db.child("/Environment").push(data)

            try:
                cursor = cnx.cursor();
                query = "INSERT INTO `device` (`macAddress`, `manufacturer`, `model`) VALUES(%s, %s, %s);";
                values = (MacAddress, 'Raspberry Pi', 'Model B+');
                result = cursor.execute(query, values)
                cnx.commit()
            except:
                print('!Could not insert a new record  to MySql\n\tError: {0}\n\t\t{1}\n\t\t{2}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]));
            finally:
                if(cnx.is_connected()):
                    cursor.close()

            try:
                cursor = cnx.cursor();
                query = "INSERT INTO `timestamp` (`date`,`time`) VALUES(%s, %s);";
                values = (date_sense, time_sense);
                result = cursor.execute(query, values)
                cnx.commit()
            except:
                print('!Could not insert a new record  to MySql\n\tError: {0}\n\t\t{1}\n\t\t{2}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]));
            finally:
                if(cnx.is_connected()):
                    cursor.close()

            try:
                cursor = cnx.cursor();
                query =   "INSERT INTO `sensor` (`timestamp`,`deviceMacAddress`, `pressure`, `temperature`, `humidity`) VALUES (LAST_INSERT_ID(), %s, %s, %s, %s);";
                values = (MacAddress, Pressure, Temperature, Humidity);
                result = cursor.execute(query, values)
                cnx.commit()
            except:
                print('!Could not insert a new record  to MySql\n\tError: {0}\n\t\t{1}\n\t\t{2}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]));
            finally:
                if(cnx.is_connected()):
                    cursor.close()

            if print_results == True:
                print("Time: {0}\tMacAddress: {1}".format(time_sense, MacAddress))
                print("\tTemperature: {0}C\tPressure: {1}Mb\tHumidity: {2}%\n\n".format(Temperature, Pressure, Humidity))
        except Exception as e:
            raise
        sleep(interval)

def pushMovementReadings(interval = 1, print_results = True):
    while(True):
        try:
            Acceleration = sense.get_accelerometer_raw()
            Orientation = sense.get_orientation()
            north = sense.get_compass()

            time_sense = time.strftime('%H:%M:%S')
            date_sense = time.strftime('%d/%m/%Y')
            data = {"MAC": MacAddress, "Date": date_sense, "Time": time_sense, "Acceleration": Acceleration, "Orientation": Orientation, "Compass": north}
            db.child("/Movement").push(data)

            if print_results == True:
                x = Acceleration['x']
                y = Acceleration['y']
                z = Acceleration['z']
                pitch = Orientation["pitch"]
                roll = Orientation["roll"]
                yaw = Orientation["yaw"]
                print("Time: {0}\tMacAddress: {1}".format(time_sense, MacAddress))
                print("\tX={0}, Y={1}, Z={2}".format(x, y, z))
                print("\tPitch {0} Roll {1} Yaw {2}\n\n".format(pitch, roll, yaw))
        except Exception as e:
            raise
        sleep(interval)

def publishToPubNub(interval=10):
	while(True):
		try:
			time_sense = time.strftime('%H:%M:%S')
			date_sense = time.strftime('%d/%m/%Y')
			Temperature = sense.get_temperature()
			Pressure = sense.get_pressure()
			Humidity = sense.get_humidity()
			Acceleration = sense.get_accelerometer_raw()
			Orientation = sense.get_orientation()
			north = sense.get_compass()
			x = Acceleration['x']
			y = Acceleration['y']
			z = Acceleration['z']
			pitch = Orientation["pitch"]
			roll = Orientation["roll"]
			yaw = Orientation["yaw"]

			data = {"MAC": MacAddress,
				"Date": date_sense,
				"Time": time_sense,
				"Temperature": Temperature,
				"Humidity": Humidity,
				"Pressure": Pressure,
				"x":x,
				"y":y,
				"z":z,
				"pitch":pitch,
				"roll":roll,
				"yaw":yaw
				}
			pubnub.publish().channel(channel).message({"eon": data}).pn_async(my_publish_callback)
		except Exception as e:
            		raise
		sleep(interval)

def deviceState():
    while True:
        Acceleration = sense.get_accelerometer_raw()
        x = Acceleration['x']
        y = Acceleration['y']
        z = Acceleration['z']

        x = round(x, 0)
        y = round(y, 0)
        z = round(z, 0)

        if abs(x) > 1 or abs(y) > 1 or abs(z) > 1:
            # Update the rotation of the display depending on which way up the Sense HAT is
            if x  == -1:
                sense.set_rotation(180)
            elif y == 1:
                sense.set_rotation(90)
            elif y == -1:
                sense.set_rotation(270)
            else:
                sense.set_rotation(0)

            sense.show_letter("!", COLOR['red'])
        else:
            sense.clear()


def joysticMovements():
    MessageSpeed = 0.05; ValueSpeed = 0.05
    TextColour = COLOR['orange'];
    while True:
        for event in sense.stick.get_events():
            # Check if the joystick was pressed
            if event.action == "pressed":

              # Check which direction
              if event.direction == "up":
                  sense.show_message("Temperature", text_colour=TextColour, scroll_speed=MessageSpeed)
                  sense.show_message("{0}C".format(round(sense.get_temperature(), 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
              elif event.direction == "down":
                  sense.show_message("Pressure", text_colour=TextColour, scroll_speed=MessageSpeed)
                  sense.show_message("{0}Mb".format(round(sense.get_pressure(), 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
              elif event.direction == "left":
                  sense.show_message("Humidity", text_colour=TextColour, scroll_speed=MessageSpeed)
                  sense.show_message("{0}%".format(round(sense.get_humidity(), 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
              elif event.direction == "right":
                  sense.show_message("Compass", text_colour=TextColour, scroll_speed=MessageSpeed)
                  sense.show_message("{0} N".format(round(sense.compass, 1)), text_colour=TextColour, scroll_speed=ValueSpeed)
              elif event.direction == "middle":
                  sense.show_letter("!", text_colour=TextColour)
              # Wait a while and then clear the screen
              sleep(0.5)

pushEnvironmentalReadings();

"""a = Process(target=joysticMovements)
a.start()

b = Process(target=deviceState)
b.start()

c = Process(target=pushEnvironmentalReadings)
c.start()

d = Process(target=pushMovementReadings)
d.start()

e= Process(target=publishToPubNub)
e.start()

a.join()
b.join()
c.join()
d.join()
e.join """

#Clossing the connection to MySQL database
if(cnx.is_connected()):
    cnx.close()
