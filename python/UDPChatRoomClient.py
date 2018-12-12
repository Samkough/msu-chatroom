from socket import *
from threading import Thread
import random

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)

def receive():
    while True:
        try:
            message, serverAddress = clientSocket.recvfrom(2048)
            print(message.decode())
        except OSError:
            break
        
def send():
    while True:
        try:
            message = input("")
            clientSocket.sendto(message.encode(), (serverName, serverPort))
        except KeyboardInterrupt:
            break
                                

print("Starting up the client...")
msg = "join"
clientSocket.sendto(msg.encode(), (serverName, serverPort))
receive_thread = Thread(target = receive)
receive_thread.start()

while True:
    send()
    if msg == "{quit}":
        False
        
receive_thread.join()
clientSocket.close()
exit()
