from socket import *

clients = list()
addrs = list()

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Server started on port " + str(serverPort) + "...")

def broadcast(msg):
    for sock in addrs:
        serverSocket.sendto(msg.encode(), (ip, port))

while True:
    msg, clientAddr = serverSocket.recvfrom(2048)
    msg = msg.decode()

    ip = clientAddr[0]
    port = clientAddr[1]
    prefix = str(ip) + ":" + str(port) + ": "

    if msg == "join":
        print("JOIN")
        addrs.append(clientAddr)
        print(clientAddr)
        broadcast(prefix + "joined!")
    elif msg == "quit":
        print("QUIT")
        del addrs[clientAddr]   
        broadcast(prefix + "quit!")
    else:
        print("OTHER")
        broadcast(prefix + msg)
