#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf8")
            print(message)
        except OSError:
            break

def send(event = None):
    message = input("")
    print(message)
    client_socket.send(bytes(message,"utf8"))
    if message == "[exit]":
        client_socket.close()
        
def quitting():
    message = "exit"
    send()

host = input('Enter host: ')
port = input('Enter port: ')
address = (host, int(port))

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(address)

receive_thread = Thread(target = receive)
receive_thread.start()
