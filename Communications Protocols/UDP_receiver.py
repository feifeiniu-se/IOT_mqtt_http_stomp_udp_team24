#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 13777))
print("UDP bound on port 13777...")

while True:
    data, addr = s.recvfrom(1024)
    w_result = open("../flask/database/rotation.txt", "a")
    w_result.write(str(data, encoding="utf-8") + "\n")
    w_result.close()
    print("Receive from %s:%s" % addr)
    print(data)
    if data == b"exit":
        s.sendto(b"Good bye!\n", addr)
        continue
    s.sendto(b"Receive rotation data: %s!\n" % data, addr)
