Hvordan installere MQTT Broker Mosquitto på Raspberry Pi


Dette er en guide til hvordan å installere MQTT megleren Mosquitto på en Raspberry Pi. Det er nødvendig å installere dette da MQTT protokollen virker sånn at man må abonnere på temaer, og dette krever en megler (broker). Mosquitto er da det klart beste alternativet, da det er den mest utbredte, stabile og anerkjente megleren. For å gjøre dette er det en fordel å ha en grunnleggende forståelse for Linux baserte systemer og ikke å ha terminal skrekk.

Utstyr som kreves:
Raspberry Pi
Internett( WiFi eller ethernet )
Tastatur og mus
Skjerm (man kan alternativt nå Raspberry Pi terminalen gjennom SSH)

Steg 1
Start opp Raspberry Pi og åpne en terminal. Oppdater enheten før du starter installering av Mosquitto.

Dette gjøres enkelt ved to kommandoer i terminal:
    sudo apt-get update
    sudo apt-get upgrade

Steg 2
Skriv inn følgende kommandoer  i terminalen, må utføres hver for seg og i rekkefølge. Ikke klipp og lim inn allt på en gang.

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



Steg 3
Test av Mosquitto ble installert korrekt.

Åpne to nye terminal vindu
Start Mosquitto: sudo/etc/init.d/mosquitto start
Terminal 1 skriv inn: mosquitto_sub -v -t "test/topic"
Terminal 2 skriv inn: mosquitto_pub -t "test/topic" -m "Hello World!"

Etter å ha gjort dette, har du opprettet en strøm som det vil kunne gå ann å abonnere på. Du har satt ett av vinduene til å abonnere på denne strømmen og det andre til å sende beskjeden “Hello World!” gjennom strømmen.

Dersom dette kommer opp er MQTT brokeren Mosquitto klar til bruk.


https://alexkychen.wordpress.com/2017/11/09/install-mosquitto-on-raspbian-stretch/




