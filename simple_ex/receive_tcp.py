#!/usr/bin/python
# Date: 2014-01-28
# From: file:///home/jessem/projects/Documentation/python-2.7.3-docs-html/library/socket.html
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50000              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
