from socket import *
from threading import Thread

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

    send_thread = Thread(target=send)
    send_thread.start()

receive_thread.join()
send_thread.join()
clientSocket.close()
exit()
