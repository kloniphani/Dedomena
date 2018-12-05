from sense_hat import SenseHat
sense = SenseHat()

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

def pushEnvironmentalReadings(interval = 5, print_results = False, decimal = 1):
    #Take readings from all three sensors and ound the values to one decimal place
    Temperature
    Pressure
    Humidity
    return round(sense.get_temperature(), 1), round(sense.get_pressure(), 1), round(sense.get_humidity(), 1);

def pushMovementReadings(interval = 5, print_results = False, decimal = 1):
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']


    from sense_hat import SenseHat
    sense = SenseHat()
    sense.clear()

    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
    return True

def deviceState():
    while True:
        acceleration = sense.get_accelerometer_raw()
    	x = acceleration['x']
    	y = acceleration['y']
    	z = acceleration['z']

    	x=round(x, 0)
    	y=round(y, 0)
    	z=round(z, 0)

        # Update the rotation of the display depending on which way up the Sense HAT is
      	if x  == -1:
      	  sense.set_rotation(180)
      	elif y == 1:
      	  sense.set_rotation(90)
      	elif y == -1:
      	  sense.set_rotation(270)
      	else:
      	  sense.set_rotation(0)

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1 or y > 1 or z > 1:
            sense.show_letter("!", COLOR['red'])
        else:
            sense.clear()

def joysticMovements():
    while True:
      for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":

          # Check which direction
          if event.direction == "up":
            sense.show_letter("U")      # Up arrow
          elif event.direction == "down":
            sense.show_letter("D")      # Down arrow
          elif event.direction == "left":
            sense.show_letter("L")      # Left arrow
          elif event.direction == "right":
            sense.show_letter("R")      # Right arrow
          elif event.direction == "middle":
            sense.show_letter("M")      # Enter key

          # Wait a while and then clear the screen
          sleep(0.5)
          sense.clear()


while True:
  # Calling a function to take all the readings
  Temperature, Pressure, Humidity = getReadings()

  message = "Temperature: " + str(Temperature) + " Pressure: " + str(Pressure) + " Humidity: " + str(Humidity)

  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.5)
