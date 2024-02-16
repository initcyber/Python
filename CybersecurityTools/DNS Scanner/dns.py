from scapy.all import *
import sys

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translated a hostname to IPV4

else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 dns.py <ip>")
	sys.exit()

def DNSScan(target):
	ans,unans = sr(IP(dst=target)/UDP(sport=5555, dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com")),timeout=2, verbose=0) #Including Source Port (sport) if we wanted to use wireshark
	if ans:
		print("Host is up at %s" %target)
		
DNSScan(target)