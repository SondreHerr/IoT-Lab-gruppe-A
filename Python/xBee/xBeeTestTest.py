import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1.0)

while True:
	#ser.write('IS \r\n')
	incoming = ser.readline().strip()
	incomingDecoded = incoming.decode('unicode_escape')
	with open('xBeeTestTestData.txt', 'w') as f:
		f.write("data %s" % incoming)
	print 'Recived data: ' + incomingDecoded


