import argparse
import time
import datetime
import sys
from influxdb import InfluxDBClient
from sense_hat import SenseHat

sense=SenseHat()
 
# Set required InfluxDB parameters.
host = "localhost" 
port = 8086
user = "root"
password = "root"
 

sampling_period = 5

def get_args():
    parser = argparse.ArgumentParser(description='Program writes measurements data from SenseHat to specified influx db.')
    parser.add_argument('-db','--database', type=str, help='Database name', required=True)
    parser.add_argument('-sn','--session', type=str, help='Session', required=True)
    now = datetime.datetime.now()
    parser.add_argument('-rn','--run', type=str, help='Run number', required=False,default=now.strftime("%Y%m%d%H%M"))
    
    # Array of all arguments passed to script
    args=parser.parse_args()
    # Assign args to variables
    dbname=args.database
    runNo=args.run
    session=args.session
    return dbname, session,runNo
    
def get_data_points():
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    acceleration = sense.get_acceleration_raw()
    orientation = sense.get_orientation()
    compass=sense.get_get_compass()

    #acceleration axes
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    #orientation 
    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']

    timestamp=datetime.datetime.utcnow().isoformat()
    #print ("{0} {1} Temperature: {2}{3}C Pressure: {4}mb Humidity: {5}%" .format(session,runNo,round(temperature,1),u'u00b0'.encode('utf8'),round(pressure,3),round(humidity,1)))
    
    # Create Influxdb datapoints (using lineprotocol as of Influxdb >1.1)
    datapoints = [
            {
                "measurement": session,
                "tags": {"runNum": runNo,
                },
                "time": timestamp,
                "fields": {
                    "temperature":temperature,"pressure":pressure,"humidity":humidity,"x":x,"y":y,"z":z,"pitch":pitch,"roll":roll,"yaw":yaw
                    }
                }
            ]
    return datapoints

dbname, session, runNo =get_args()   
print "Session: ", session
print "Run No: ", runNo
print "DB name: ", dbname

# Initialize the Influxdb client
client = InfluxDBClient(host, port, user, password, dbname)
        
try:
     while True:
        # Write datapoints to InfluxDB
        datapoints = get_data_points()
        bResult=client.write_points(datapoints)
        print("Write points {0} Bresult:{1}".format(datapoints,bResult))
        
        sense.show_message("dedomena")
        time.sleep(sampling_period)
        
        # Run until keyboard ctrl-c
except KeyboardInterrupt:
    print ("Program stopped by keyboard interrupt [CTRL_C] by user. ")
    
