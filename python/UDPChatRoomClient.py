from socket import *
from threading import Thread

def receive():
    while True:
        try:
            message, serverAddress = clientSocket.recvfrom(2048) # waits for server to send a message and doesn't move forward
            print(message.decode())
        except OSError:
            break

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("Starting up the client...")
msg = "join"
clientSocket.sendto(msg.encode(), (serverName, serverPort))
receive_thread = Thread(target = receive)
receive_thread.start()

while True:
    msg = input("")
    clientSocket.sendto(msg.encode(), (serverName, serverPort))
    if msg == "quit":
        False

receive_thread.join() # keeps the thread going
clientSocket.close()
exit()
