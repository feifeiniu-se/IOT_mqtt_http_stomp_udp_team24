import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    w_result = open("../flask/database/temperature.txt", "a")
    w_result.write(str(msg.payload, encoding="utf-8")+"\n")
    w_result.close()
    print(msg.topic + " " + str(msg.payload, encoding="utf-8"))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("47.103.20.207", 1883, 600)
client.publish('temperature_response', payload='1 temperature received', qos=0)
client.subscribe('temperature_sender', qos=0)
client.loop_forever()

