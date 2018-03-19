import paho.mqtt.client as mqtt
import time
from sense_hat import SenseHat

sense = SenseHat()

# SETTING UP A MQTT CLIENT
client = mqtt.Client("python_pub")

# SETTING USERNAME AND PASSWORD FOR MQTT
client.username_pw_set(username="pi", password="raspberry")

# SETTING SERVER UP TO PUBLISH TO 10.0.0.19, THIS NEEDS TO BE YOUR PIS IP ADDRESS
# TODO
client.connect("10.0.0.19", 1883)
client.loop_start()

try:

    while True:
        # GENERATING TOPIC AND PUBLISHING
        #
        # TEMPERATURE
        temperature = sense.get_temperature()
        temperature = round(temperature, 2)
        client.publish("sense/temperature", temperature + "C")

        # HUMIDITY
        humidity = sense.get_humidity()
        humidity = round(humidity, 2)
        client.publish("sense/humidity", humidity + "%")

        # PRESSURE
        pressure = sense.get_pressure()
        pressure = round(pressure, 2)
        client.publish("sense/pressure", pressure + "Millibar")
        # WAIT 10 SECONDS FOR NEW READ
        time.sleep(10)

except KeyboardInterrupt:
    print("interrupted")
    client.loop_stop()
