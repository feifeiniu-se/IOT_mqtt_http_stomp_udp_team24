# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

def UDP_sender(value):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ("47.103.20.207", 13777)
    # addr = ("127.0.0.1", 13777)
    s.sendto(value.encode(), addr)
    response, addr = s.recvfrom(1024)
    print(response.decode())
    if value == "exit":
        print("Session is over from the server %s:%s\n" % addr)

    s.close()
