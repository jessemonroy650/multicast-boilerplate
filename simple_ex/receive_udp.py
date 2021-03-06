#!/usr/bin/env python
# DATE: 2014-01-26
# FROM:
# https://wiki.python.org/moin/UdpCommunication
import socket

UDP_IP = ""
UDP_PORT = 5432

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
