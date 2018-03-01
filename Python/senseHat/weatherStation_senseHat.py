
from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.clear()


try:
    while True:
        temp = sense.get_temperature()
        temp = round(temp, 1)
        print("Temperature in C: ", temp)
        
        humidity = sense.get_humidity()
        humidity = round(humidity, 1)
        print("Humidity: " , humidity)
        
        pressure = sense.get_pressure()
        pressure = round(pressure, 1)
        print("Pressure: ", pressure)
        
        time.sleep(1)

Except KeyboardInterrupt:
    pass


sense.show_message("Temperature" + temp)

sense.clear()