from sense_hat import SenseHat
sense = SenseHat()

# Define the colours in a dictionary
COLOR = {
    'red' : (255, 0, 0)
    'green': (0, 255, 0)
    'blue' : (0, 0, 255)
    'black': (0, 0, 0)
    'white' : (255, 255, 255)
    'orange': (255, 165, 0)
    'yellow' : (255, 225, 0)
    'cyan': (0, 255, 255)
    'violet': (238, 130, 238)
    'brown' : (165, 42, 42)
    'purple': (128, 0, 128)
}

def getReadings():
    #Take readings from all three sensors and ound the values to one decimal place, Then return the reading
    return round(sense.get_temperature(), 1),
        round(sense.get_pressure(), 1),
        round(sense.get_humidity(), 1);

while True:
  # Calling a function to take all the readings
  t, p, h = getReadings()

  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

  if t > 18.3 and t < 26.7:
    bg = COLOR['green']
  else:
    bg = COLOR['red']

  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, back_colour=bg)
