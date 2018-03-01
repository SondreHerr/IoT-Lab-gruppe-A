"""AUTHOR SONDRE HERREDSVELA"""
"""IMPORTING LIBRARYS, CLEARING AND SETTING THE HAT AS A VAR"""
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()


"""DEFINING COLORS"""
red = (255, 0, 0)
green = (0, 255, 0)
orange = (255, 215, 0)
txt = (0, 0, 0)

"""RUNS AND PRINTS TEMP"""
while True:
    
    """GETTING TEMP"""
    temp = sense.get_temperature()
    temp = int(temp)
    
    if temp > 32:
        sense.show_message(str(temp) + "C! Major alarm", text_colour=txt, back_colour=red)
    elif temp >= 28 and temp <= 32:
        sense.show_message(str(temp) + "C! Minor alarm", text_colour=txt, back_colour=orange)
    else:
        sense.show_message(str(temp) + "C", text_colour=txt, back_colour=green)
    
    sleep(5)

        