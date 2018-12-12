from socket import *

clients = list()
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Server started on port " + str(serverPort) + "...")

def broadcast(msg):
    for sock in clients:
        serverSocket.sendto(msg.encode(), sock)
        print(sock) # testing to see all sockets

while True:
    msg, clientAddr = serverSocket.recvfrom(2048)
    msg = msg.decode()

    ip = clientAddr[0]
    port = clientAddr[1]
    prefix = str(ip) + ":" + str(port) + ": "

    if msg == "join":
        print("JOIN")
        
        cond = 0
        for client in clients:
            if clientAddr == client:
                cond = 1
        if cond == 0:
            print("Not duplicate")
            clients.append(clientAddr)
        else:
            print("Duplicate")
            
        # print(clientAddr)
        broadcast(prefix + "joined!")
    elif msg == "{quit}":
        print("QUIT")
        del clients[clientAddr]
        broadcast(prefix + " quit!")
    else:
        print("OTHER")
        broadcast(prefix + msg)
