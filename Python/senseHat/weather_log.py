from sense_hat import SenseHat
from time import asctime
from time import sleep

sense = SenseHat()

temp = round(sense.get_temperature())
humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())
message = 'Temperature is %d C Humidity is %d percent Pressure is %d mbars' %(temp,humidity,pressure)

sense.show_message(message, scroll_speed=(0.08),text_colour=[200,0,200], back_colour= [0,0,200])
sense.clear()

while True:
    log = open("weather.txt", "a")
    now = str(asctime())
    log.write(now + " " + message + "\n")
    print(message)
    log.close()
    sleep(30)
    
log.close()