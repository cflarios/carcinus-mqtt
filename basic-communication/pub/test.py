import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("test.mosquitto.org", 1883, 60)

# send a message to the raspberry/topic every 1 second, 5 times in a row
for i in range(5):
    # the four parameters are topic, sending content, QoS and whether retaining the message respectively
    client.publish('raspicarcinus/topic', payload=i, qos=0, retain=False)
    print(f"send {i} to raspicarcinus/topic")
    time.sleep(1)

client.loop_forever()
