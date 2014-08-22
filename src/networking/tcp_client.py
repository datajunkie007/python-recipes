#!/usr/bin/env

#
# Demonstrates example TCP client.
# Connects to the port 20000 on localhost and sends string.
# Prints received message.
#

from socket import socket, AF_INET, SOCK_STREAM 

def test_tcp_client():
  s = socket(AF_INET, SOCK_STREAM)
  s.connect(('localhost', 20000))
  s.send(b'Hello')
  print s.recv(8192)
  

if __name__ == '__main__':
  test_tcp_client()
