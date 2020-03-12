import socket, time

HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket()
client_socket.connect((HOST, PORT))
data = 'Hello Data!'
client_socket.sendall(data.encode())
client_socket.close()
