from sense_hat import SenseHat
from time import sleep
from time import asctime

sense = SenseHat()
sense.clear()

humidity = sense.get_humidity()
humidity = int(humidity) 
print(humidity)

b = (0, 0, 255)
g = (0, 255, 0)

bkg_blue= [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
    ]
bkg_green = [
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g
    ]
bkg_lol = [
    g,g,g,b,b,g,g,g,
    g,g,g,b,b,g,g,g,
    g,g,g,b,b,g,g,g,
    g,g,g,b,b,g,g,g,
    g,g,g,b,b,g,g,g,
    g,b,b,b,b,b,b,g,
    b,b,b,b,b,b,b,b,
    g,b,b,g,g,b,b,g
    ]



while True:
    if humidity < 10:
        sense.set_pixels(bkg_blue)
    elif humidity < 14 and humidity > 20:
        sense.set_pixels(bkg_green)
    else:
        sense.set_pixels(bkg_lol)
        
    
