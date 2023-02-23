#!/bin/python3
#Sockets
import socket
import sys
from datetime import datetime

#Define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
    print("Invalid run attempt")
    print("Syntax: python3 scanner.py <ip>")

#Adding to it
print("-"*50)
print("Scanning: " + target)
print("Time Started: " +str(datetime.now()))
print("-"*50)

try:
    for port in range(1,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nQuitting Program")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    
