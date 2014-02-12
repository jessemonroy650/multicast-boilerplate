#!/usr/bin/python
# Date: 2014-01-28
# From: file:///home/jessem/projects/Documentation/python-2.7.3-docs-html/library/socket.html
# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
HOST = '10.15.1.154'
PORT = 50000              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)