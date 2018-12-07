from socket import *
from threading import Thread

def handle():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf8") # waits for server to send a message and doesn't move forward
            print(message)
            Thread(target = send).start()
        except OSError:
            break

def send():
    message = input("")
    client_socket.send(bytes(message,"utf8"))
    if message == "[exit]":
        client_socket.close()

host = input('Enter host: ')
port = input('Enter port: ')
if not port:
    port = 33000
else:
    port = int(port)

address = (host, port)

client_socket = socket(AF_INET, SOCK_STREAM)
print(client_socket)
client_socket.connect(address)

if __name__ == "__main__":
    print("Starting up the client...")
    receive_thread = Thread(target = handle)
    receive_thread.start()
    receive_thread.join() # keeps the thread going
    exit()
