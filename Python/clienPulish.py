import paho.mqtt.client as mqtt
import time

from sense_hat import SenseHat

sense = SenseHat()

#SETTING UP A MQTT CLIENT
client = mqtt.Client("python_pub")

#SETTING USERNAME AND PASSWORD FOR MQTT
client.username_pw_set(username="pi", password="raspberry")

#SETTING SERVER UP TO PUBLISH TO 192.168.1.32
client.connect("192.168.1.32", 1883)
client.loop_start()

try:

	while True:
		#GENERATING TOPIC AND PUBLISHING

		#TEMPERATURE
		client.publish("sense/temp", sense.get_temperature())
		#HUMIDITY
		client.publish("sense/humid", sense.get_humidity())
		#WAIT 10 SECONDS FOR NEW READ
		time.sleep(10)
except KeyboardInterrupt:
	print("interrupted")
	client.loop_stop()
