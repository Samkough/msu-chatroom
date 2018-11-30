#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
client_addresses = {}

host = ''
port = 33000
address = (host, port)

server = socket(AF_INET, SOCK_STREAM)
server.bind(address)

def accept():
    # waits for incoming connections
    # once it gets one, logs the connection and sends client message
    # stores client in list
    # start to handle thread for client in handle()

def handle(client):
    # save client name
    # broadcast to all clients that new client entered
    # receive messages from client (if quits, it quits)
    # if quits, close the connecction with client
    # delete entry of client in list
    # broadcast to all clients that client left the chat

def broadcast(msg, client_name=""):  # prefix is for name identification.
    # sends message to all clients

if __name__ == "__main__":
    server.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target = accept)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.close()
