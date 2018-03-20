ChannelID = 'your channel ID'

apikey = 'your API key'

m = mqtt.Client(ClientID, 120)

m: connect("mqtt.thingspeak.com", 1883, 0, function(client) print("connected") m: publish("channels/"..ChannelID.."/publish/"..apikey, "field1="..temp.."&amp;field2="..humi, 0, 0) m: close() end)
