#!/bin/python3

import sys #Allows us to enter command line arguments, among other things
import socket #Allows us to connect to ports/ip/etc
from datetime import datetime

#Define our target
#Usage : python3 scanner.py <ip>
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translated a hostname to IPV4

else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()

#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: " +str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,1000):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is ipv4, SOCK_STREAM is port
		socket.setdefaulttimeout(1) #is a float (ex. 1.5)
		result = s.connect_ex((target,port)) #Returns Error Indicator
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()
