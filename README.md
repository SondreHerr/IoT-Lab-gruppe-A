# IoT-Lab-gruppe-A
For kode og konfig


Lenke til hvordan å konfigurer Mosquitto MQTT Broker på en Raspberry Pi
https://iotbytes.wordpress.com/mosquitto-mqtt-broker-on-raspberry-pi/


Node-RED download
bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)


Snadderboard:

https://freeboard.io/board/YTray7

http://dweet.io/follow/sondreherredsvela


Intressange greie:
http://pdwhomeautomation.blogspot.no/2015/03/using-fitbit-api-on-raspberry-pi-with.html

Recieving XBee data on RPi:
http://www.raspberry-pi-geek.com/Archive/2015/12/Analyzing-sensor-readings-with-an-XBee-wireless-connection/(offset)/2

### https://github.com/jeancarl/node-red-labs/tree/master/lab-sense-hat/node-red-dashboard









cd ~

wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key

sudo apt-key add mosquitto-repo.gpg.key

cd /etc/apt/sources.list.d/

sudo wget http://repo.mosquitto.org/debian/mosquitto-stretch.list

sudo apt-get update


cd ~

wget http://security.debian.org/debian-security/pool/updates/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u7_armhf.deb

sudo dpkg -i libssl1.0.0_1.0.1t-1+deb8u7_armhf.deb

wget http://ftp.nz.debian.org/debian/pool/main/libw/libwebsockets/libwebs
ockets3_1.2.2-1_armhf.deb

sudo dpkg -i libwebsockets3_1.2.2-1_armhf.deb

sudo apt-get install mosquitto mosquitto-clients
