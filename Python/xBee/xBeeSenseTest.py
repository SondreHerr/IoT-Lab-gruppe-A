import serial

ser = serial.Serial('/dev/ttyUSB0')
print(ser.name)
# USB PORTS SONDRE MAC
#/dev/tty.usbserial-AL033CVS
#/dev/tty.usbserial-AL033DVI

# COORDINATOR MAC ADDRESS: 0013A2004148162B
# ROUTER MAC ADDRESS: 0013A20041481644

# IF CONNECTED TO D3
# FRAME ON: 7E 00 10 17 AB 00 13 A2 00 41 48 16 44 FF FE 02 44 33 05 2A
# FRAME OFF: 7E 00 10 17 AB 00 13 A2 00 41 48 16 44 FF FE 02 44 33 04 2B

# RAW DATA
on = "7E 00 10 17 AB 00 13 A2 00 41 48 16 44 FF FE 02 44 33 05 2A"
off = "7E 00 10 17 AB 00 13 A2 00 41 48 16 44 FF FE 02 44 33 04 2B"

# REMOVE SPACES
messageOn = "".join(on.split())
messageOff = "".join(off.split())

# MAKE IT INTO BYTES USABLE IN SERIAL COMMUNICATION(BREAKDOWN DRIVE ME INSAAAANEEE)
messageOn = messageOn.decode("hex")
messageOff = messageOff.decode("hex")

print messageOn
print messageOff
