import time

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("mqtt Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

def mqtt_sender(value):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("47.103.20.207", 1883, 600)
    client.publish('temperature_sender', payload=value, qos=0)
    client.subscribe('temperature_response', qos=0)
    client.disconnect()
# mqtt_sender("hello")