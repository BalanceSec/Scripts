 #!/bin/python3
#Sockets
import socket

host = '127.0.0.1' #loopback addy
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock_stream is a port
s.connect((host,port))
