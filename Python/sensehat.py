from sense_hat import SenseHat
import requests
import time

#https://dweet.io/dweet/for/

sense = SenseHat()

def readings():
	temp = sense.get_temperature()
	temp = round(temp, 2)
	temp_str = str(temp)
	print("Temperature in C: ", temp)

	humidity = sense.get_humidity()
	humidity = round(humidity, 2)
	humidity_str = str(humidity)
	print("Humidity: " , humidity)

	pressure = sense.get_pressure()
	pressure = round(pressure, 2)
	pressure_str = str(pressure)
	print("Pressure: ", pressure)
	print("Str: ", pressure_str)

	url = "https://dweet.io/dweet/for/sondreherredsvela?" + "Temperatur=" + temp_str + "&Humidity=" + humidity_str + "&Pressure=" + pressure_str

	r = requests.post(url)

while True:
	readings()
	time.sleep(10)
	print("Readings recorded")
