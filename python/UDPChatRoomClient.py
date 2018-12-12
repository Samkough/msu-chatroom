from socket import *
from threading import Thread
import random

serverName = 'localhost'
serverPort = 5000
serverSocket = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)

def receive():
    while True:
        try:
            msg, serverAddr = clientSocket.recvfrom(2048)
            print(msg.decode())
        except OSError:
            break
        
def send():
    while True:
        try:
            msg = input("")
            clientSocket.sendto(msg.encode(), serverSocket)
            if msg == "{quit}":
                False
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    print("Client started...")
    msg = "join"
    clientSocket.sendto(msg.encode(), serverSocket)
    
    receive_thread = Thread(target=receive)
    receive_thread.start()

    print("receive_thread started\n")
    
    send_thread = Thread(target=send)
    send_thread.start()

    print("send_thread started\n")

print("receive_thread join starts\n")
receive_thread.join()
print("receive_thread join ends")

print("send_thread join starts")
send_thread.join()
print("send_thread join ends")

clientSocket.close()
exit()
