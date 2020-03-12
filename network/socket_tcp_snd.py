#!/usr/bin/env python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 9999))

data = 'Hello socket'
client_socket.sendall(data.encode())

data = client_socket.recv(1024)
print('Client recv:', data.decode('utf-8'))
client_socket.close()
