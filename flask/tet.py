from Scripts.coapserver import CoAPServer

server = CoAPServer("47.103.20.207", 5683, multicast = False)

# print(server.receive_request(10))
server.listen(10)
server.close()