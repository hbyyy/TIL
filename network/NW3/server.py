import socket

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 9999))
server_socket.listen()
client_socket, addr = server_socket.accept()
print('connected by ', addr)

while True:
    data = client_socket.recv(4096)
    if not data:
        break;
    print(data.decode())
client_socket.close()
server_socket.close()
