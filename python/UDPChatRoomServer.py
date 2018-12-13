from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
clients = list()

print("Server started on port " + str(serverPort) + "...")

def broadcast(prefix, msg):
    full_msg = prefix + " " + msg
    print(full_msg)
    for sock in clients:
        serverSocket.sendto(full_msg.encode(), sock)

while True:
    msg, clientAddr = serverSocket.recvfrom(2048)
    msg = msg.decode()

    ip = clientAddr[0]
    port = clientAddr[1]
    prefix = str(ip) + ":" + str(port) + ":"
    prefix_no_colon = str(ip) + ":" + str(port)

    if msg == "join":
        cond = 0
        for sock in clients:
            if clientAddr == sock:
                cond = 1

        if cond == 0:
            broadcast(prefix_no_colon, " joined the MSU Chatroom!")
            clients.append(clientAddr)
        else:
            broadcast(prefix_no_colon, "is a duplicate!")
    elif msg == "{quit}":
        clients.remove(clientAddr)
        print("Clients left: ", clients)
        broadcast(prefix_no_colon, "quit!")
    else:
        broadcast(prefix, msg)
