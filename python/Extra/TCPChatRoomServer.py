from socket import *
from threading import Thread

def accept():
    while True:
        client, client_addr = server.accept()
        print(str(client) + " has connected.")
        client.send(bytes("Welcome to the MSU Chatroom! Please enter your name:", "utf8"))
        client_addresses[client] = client_addr
        Thread(target = handle, args = (client,)).start()

def handle(client):
    name = client.recv(1024).decode("utf8")
    client.send(bytes("Welcome " + str(name) + "! To exit, type [exit].", "utf8"))
    bc_message = str(name) + "joined the chat!"
    broadcast(bytes(bc_message, "utf8"))

    clients[client] = name
    while True:
        msg = client.recv(1024)
        if msg != bytes("[exit]", "utf8"):
            broadcast(msg, str(name) + ": ")
        else:
            client.send(bytes("[exit]", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes(str(name) + " has left the chat.", "utf8"))
            break

def broadcast(msg, client_name=""):
    for sock in clients:
        sock.send(bytes(client_name, "utf8") + msg)

clients = {}
client_addresses = {}

host = ''
port = 33000
address = (host, port)

server = socket(AF_INET, SOCK_STREAM)
server.bind(address)

if __name__ == "__main__":
    server.listen(5)
    print("Waiting for connection...")
    accept_thread = Thread(target = accept)
    accept_thread.start()
    accept_thread.join()
    server.close()
