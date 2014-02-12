#!/usr/bin/env python
#
#
import time
import socket

MCAST_GRP = '224.0.0.1'
MCAST_PORT = 5432
# Actually the maxium number of hops
TTL_VALUE = 2
myhost = 'Rover'

tdata = repr(time.time())

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, TTL_VALUE)
sock.sendto("Hello World at:" + tdata + " from " + myhost, (MCAST_GRP, MCAST_PORT))
print "Hello World - sent"

exit
