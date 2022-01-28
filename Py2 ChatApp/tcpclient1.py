#!/usr/bin/env python

import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print "Pass moar args aaaaaaarrrrrrrrrrrrggggggggggggg"

IP_addr = str(sys.argv[1])
port = int(sys.argv[2])

client.connect((IP_addr, port))
while True:
    #print "Us: ", client.send(sys.stdin.readline())
    client.send(raw_input("Us: "))
    #sys.stdout.flush()
    #message = sys.stdin.readline()
    #client.send(message)
    print "Them:", client.recv(2048)

client.close()
