#!/usr/bin/env python

#
# Code snippet demonstrating usage of socketserver
# Server that communicates with clients using the TCP Internet protocol.
#

#
# Caution: In Python2 use SocketServer, and use socketserver in Python3.
#
from SocketServer import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler): 
    def handle(self):
        print('Got connection from', self.client_address) 
        while True:
           msg = self.request.recv(8192) 
           if not msg:
               break
           self.request.send(msg)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler) 
    serv.serve_forever()