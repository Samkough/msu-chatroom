from socket import *
from threading import Thread

serverName = 'localhost'
serverPort = 5000
serverSocket = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)

def receive():
    running = True
    while running:
        try:
            msg, serverAddr = clientSocket.recvfrom(2048)
            print(msg.decode())
        except OSError:
            break

def send():
    running  = True
    while running:
        try:
            msg = input("")
            clientSocket.sendto(msg.encode(), serverSocket)
            if msg == "{quit}":
                clientSocket.close()
                running = False
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    print("Client started...")
    msg = "join"
    clientSocket.sendto(msg.encode(), serverSocket)
    
    receive_thread = Thread(target=receive)
    receive_thread.start()
    send_thread = Thread(target=send)
    send_thread.start()
    
    receive_thread.join()

    clientSocket.close()
    exit()
