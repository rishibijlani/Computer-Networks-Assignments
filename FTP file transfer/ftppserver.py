import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

while True:
	client_socket, addr = server_socket.accept()
	with open('mytext.txt', 'rb') as f:
		client_socket.sendfile(f, 0)
	client_socket.close()
