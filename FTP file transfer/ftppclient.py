import socket

CHUNK_SIZE = 8 * 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 12345))
chunk = sock.recv(CHUNK_SIZE)
while chunk:
    with open('gg.txt', 'wb') as f:
     f.write(chunk)
    chunk = sock.recv(CHUNK_SIZE)
sock.close()
#with open('gg.bin', 'wb') as f:
#	f.write(chunk)
