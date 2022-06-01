import paho.mqtt.client as mqtt
import webbrowser
import sys



gelen_bilgi = []
latitute_str = []
longitute_str = []
latitute = 0.0
longitute = 0.0
map_link = []

f = open("olacak.txt", "w")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

   
    client.subscribe("deneme",1)


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    global gelen_bilgi
    gelen_bilgi = str(msg.payload.decode("utf-8"))
    print(gelen_bilgi)
    #gecici = gelen_bilgi.split(":")
    #print(gecici)
    global latitute, longitute, map_link
    global f
    latitute_str = gelen_bilgi[12:19]
    longitute_str = gelen_bilgi[23:30]
    print(latitute_str)
    print(longitute_str)
    gec = [latitute_str, longitute_str]
    print(gec)
   # latitute  = float(gecici[1])
   # longitute = float(gecici[2])
    f.write(latitute_str)
    f.write(",")
    f.write(longitute_str)
    f.write("\n")
    latitute = float(latitute_str)
    longitute = float(longitute_str)
    #map_link = 'http://maps.google.com/?q=' + latitute_str + ',' + longitute_str
    #print("<<<<<<<<press ctrl+c to plot location on google maps>>>>>>\n")

#try:    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)

    
client.loop_forever()
f.close()

#except KeyboardInterrupt:
 #   webbrowser.open(map_link)
  #  sys.exit(0)