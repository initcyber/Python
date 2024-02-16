# DNS Scanner

This uses scapy to scan for open DNS ports. This is just a subset of the modules available in scapy.

Basic usage is: 
```bash
python dns.py [IP Address]
```

This is useful for finding open DNS ports on a particular webhost/IP address. This code could be modified further to scan through a list of IP's or even check for DNS resolution on different ports outside of "53"