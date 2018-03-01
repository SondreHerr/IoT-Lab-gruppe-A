from sense_hat import SenseHat
from time import asctime
from time import sleep

sense = SenseHat()

while True:
    orientation = sense.get_orientation()
    
    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']
    
    print("pitch={0}, roll={1}, yaw={2}".format(pitch,yaw,roll))
    
    message = "pitch={0}, roll={1}, yaw={2}".format(pitch,yaw,roll)
    
    sense.show_message(message)
    log = open("orientation.txt", "a")
    now = str(asctime())
    log.write(now + " " + message + "\n")
    print(message)
    log.close()
    sleep(30)
    
log.close()

    
    