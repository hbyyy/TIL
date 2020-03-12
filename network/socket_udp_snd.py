import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'Hello UDP!'

dest = ('127.0.0.1', 9999)
client_socket.sendto(data.encode(), dest)
client_socket.close()
