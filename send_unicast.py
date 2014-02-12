#!/usr/bin/env python
# FROM:
# http://code.google.com/p/unladen-swallow/source/browse/branches/release-2009Q1-maint/Demo/sockets/unicast.py
#
import socket
import sys, time
from socket import *

UDP_IP = "127.0.0.1"
UDP_IP = "10.15.1.154"
MYPORT = 5000
MYSLEEPTIME = 8 # in seconds

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))

while 1:
    data = repr(time.time()) + '\n'
    s.sendto(data, (UDP_IP, MYPORT))
    print "sent>" + data
    time.sleep(MYSLEEPTIME)
