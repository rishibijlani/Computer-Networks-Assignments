#!/usr/bin/env python

import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_addr = '0.0.0.0'
port = 9001

server.bind((IP_addr, port))
server.listen(5)

conn, addr = server.accept()
print addr[0] + " connected from port " + str(addr[1])
while True:
    message = conn.recv(2048)
    print "Client:", message
    #message = sys.stdin.readline()
    #conn.send(message)
    #print "Us: ", message
    #print "Us: ", conn.send(sys.stdin.readline())
    conn.send(raw_input("Us: "))

conn.close()
server.close()
