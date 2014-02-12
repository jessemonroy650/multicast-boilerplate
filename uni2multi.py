#!/usr/bin/env python
# DATE: 2014-01-26
# FROM:
# https://wiki.python.org/moin/UdpCommunication
import socket
import time

myhost     = 'Rover'
maxPacketSz = 1500
#
UDP_IP = "127.0.0.1"
UDP_PORT = 5000
#
MCAST_GRP = '224.0.0.1'
MCAST_PORT = 5432
# Actually the maxium number of hops
TTL_VALUE = 2

# setup socket to receive UDP
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# setup socket to send Multicast
sndsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sndsock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, TTL_VALUE)

#
print "Starting UDP (unicast) on:" + UDP_IP +" to Multicast:" + MCAST_GRP

while True:
    data, addr = sock.recvfrom(maxPacketSz) # buffer size is 1500 bytes
    #         while data[-1:] == '\0': data = data[:-1] # Strip trailing \0's
    sndsock.sendto(data + " from " + myhost, (MCAST_GRP, MCAST_PORT))
    print "received message:", data


