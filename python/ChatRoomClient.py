#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

host = input('Enter host: ')
port = input('Enter port: ')

address = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target = receive)
receive_thread.start()

def receive():
    # receiving message from server

def send():
    # send message to server

def quit(event=None):
    # quitting
