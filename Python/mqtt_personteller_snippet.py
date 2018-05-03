import paho.mqtt.client as mqtt
import time

# SETTING UP A MQTT CLIENT
client = mqtt.Client("python_publisher")

# SETTING USERNAME AND PASSWORD FOR MQTT
client.username_pw_set(username="pi", password="raspberry")

# SETTING SERVER UP TO PUBLISH TO 192.168.1.41, THIS NEEDS TO BE YOUR PIS IP ADDRESS
client.connect("192.168.1.41", 1883)
client.loop_start()

try:
    while True:
        # GENERATING TOPIC AND PUBLISHING
        #
        client.publish("personteller/antall", total + " personer i rommet")
        # WAIT 10 SECONDS FOR NEW READ
        time.sleep(10)

except KeyboardInterrupt:
    print("interrupted")
    client.loop_stop()
