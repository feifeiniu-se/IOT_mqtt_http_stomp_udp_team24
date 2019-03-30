import datetime

#just for development environment, simulate the data frame
import time

import serial

from IOT.transport.STOMP_sender import STOPM_sender
from IOT.transport.UDP_sender import UDP_sender
from IOT.transport.http_sender import HTTP_sender
from IOT.transport.mqtt_sender import mqtt_sender

t = serial.Serial('com4',9600)

for i in range(120):
    value = t.readline()
    print(value)
    theTime = time.time()
    data = value.strip().split()
    if bytes.decode(data[0]) != "light":
        print("skip")
        continue

    temperature = bytes.decode(data[9]) + "," + str(theTime)
    humdity = bytes.decode(data[7]) + "," + str(theTime)
    light = bytes.decode(data[1]) + "," + str(theTime)
    rotation = bytes.decode(data[3]) + "," + str(theTime)
    led = bytes.decode(data[5]) + "," + str(theTime)
    buzzer = bytes.decode(data[11]) + "," + str(theTime)
    print("temperature: ", temperature)
    print("humdity: ", humdity)
    print("light: ", light)
    print("rotation: ", rotation)
    print("led: ", led)
    print("buzzer: ", buzzer)


    mqtt_sender(temperature)#mqtt send temperature
    STOPM_sender(humdity)#STOMP send humdity
    HTTP_sender(light)#HTTP send light sensor
    UDP_sender(rotation)#UDP send rotation sensor
    time.sleep(1)