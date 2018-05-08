from sense_hat import SenseHat
import time
import requests

sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
orange = (255, 215, 0)
txt = (0, 0, 0)


def readData():

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

        if temp > 36:
                sense.show_message(str(temp) + "C! Major alarm", text_colour=txt, back_colour=red)
        elif temp >= 33 and temp <= 36:
                sense.show_message(str(temp) + "C! Minor alarm", text_colour=txt, back_colour=orange)
        else:
                sense.show_message(str(temp) + "C", text_colour=txt, back_colour=green)


        url = "https://dweet.io/dweet/for/iot_lab_gruppe_a_miljo?" + "Temperatur=" + temp_str + "&Humidity=" + humidity_str + "&Pressure=" + pressure_str

        r = requests.post(url)

while True:
        readData()
        time.sleep(10)
