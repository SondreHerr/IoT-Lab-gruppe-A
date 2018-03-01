from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

"""GETTING TEMP"""
temp = sense.get_temperature()
temp = int(temp)
print(temp)
"""END TEMP"""

"""GETTING HUMIDITY"""
humidity = sense.get_humidity()
humidity =  int(humidity)
print(humidity)

"""TEXT COLOR"""
blue = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
"""TEXT COLOR END"""



sense.show_message(str(temp) + "C", text_colour=yellow, back_colour=blue)
sense.show_message(str(humidity) + "%", text_colour=green)