from sense_hat import SenseHat
import time
import datetime
from time import sleep

import pyrebase
import sys


config = {
	"apiKey": "AIzaSyCohsgXa-m4KvMQPQMFnJr9mClQKlTA3BQ",
    	"authDomain": "raspberrypi-e763b.firebaseapp.com",
    	"databaseURL": "https://raspberrypi-e763b.firebaseio.com",
    	"storageBucket": "raspberrypi-e763b.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


sense = SenseHat()

while True:
	time_sense = time.strftime('%H:%M:%S')
	date_sense = time.strftime('%d/%m/%Y')
	humidity = round((sense.get_humidity()*64)/100,1)
	temperature = round(sense.get_temperature(),1)
	pressure = round(sense.get_pressure(),1)
	
	
	print("Humidity %s " %humidity)
	print("Temperature %s Degrees Celcius" %temperature)
	print("Pressure: %s Millibars" %pressure)
	print

	data = {"Date": date_sense,"Time": time_sense, "Temperature": temperature, "Humidity": humidity, "Pressure": pressure}
	db.child("/message").push(data)	

	sense.show_message("Hello world")
	
	time.sleep(5)
	