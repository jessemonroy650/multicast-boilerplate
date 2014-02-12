#!/usr/bin/env python
# DATE: 2014-01-26
# FROM:
# https://wiki.python.org/moin/UdpCommunication
import socket

UDP_IP   = "127.0.0.1"
UDP_PORT = 5432
MESSAGE  = "Hello, World! udp from Rover"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

exit