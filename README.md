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



lora


1. Klone github repository
I terminalen skriv kommandoen:
	git clone https://github.com/bokse001/dual_chan_pkt_fwd

2. Tillat SPI
	sudo raspi-config
Gå deretter ned på “Interfacing options” og enable SPI

3. Innstaller wiringpi
	sudo apt-get install wiringpi

4. Konfigurer innstillinger for gateway
	cd ~/dual_chan_pkt_fwd
	nano global_conf.json
i denne filen skal du endre et par pin assignments:
“pin_nss”:6
“pin_dio0”:7
“pin_nss_2”:6
“pin_dio0_2”:7
“pin_rst”:3
“pin_led1”:4

Deretter setter du inn latitude og longitude på posisjonen av LoRa gatewayen. Om den befinnes på UiS vil det være:
lat: 58.937875
lon: 5.697094

name og andre ting endrer du ettersom hva du ønsker.

deretter lagre filen ved å trykke ctrl+O og trykk enter
skriv
	make
	./dual_chan_pkt_fwd
For å starte gatewayen

Nå er den up and running, og du vil finne den på https://www.thethingsnetwork.org/# i den posisjonen du anga i konfigurasjonen
