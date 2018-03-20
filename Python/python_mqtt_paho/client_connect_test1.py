#!python3
import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
	print("log" + buf)


def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected OK")
	else:
		print("Bad connection Returned code=", rc)

def on_disconnec(client, userdata, flags, rc=0):
	print("DisConnected result code ", str(rc)

#Setting this Raspberry Pis ip address as te broker
broker = "192.168.1.32"

#Creating a new client named senseHat
client = mqtt.Client("senseHat")

# Binding callback functions
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_log = on_log

print("Connecting to broker "  + broker)
# Connecting to broker
client.connect(broker)

# Starting loop
client.loop_start()

client.subscribe("sense/temp")
client.publish("sense/temp", "Hei")

time.sleep(4)

# Stopping loop
client.loop_stop()

client.disconnect()
