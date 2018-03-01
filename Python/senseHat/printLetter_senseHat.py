from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
r = randint(0, 255)
sense.show_letter("j", (r, 0, 0))
sleep(2)

r = randint(0, 255)
sense.show_letter("e", (0, r, 0))
sleep(2)

r = randint(0, 255)
sense.show_letter("w", (0, 0, r))
sleep(2)
sense.clear()