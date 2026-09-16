1. What is ipaddress?

ipaddress is a built-in Python module used to work with:

IPv4 addresses
IPv6 addresses
Networks
Subnets
Hosts
IP address comparison
Network membership
Subnet calculations

You don't need to install it.

import ipaddress

Think of it as:

ipaddress = Python's toolkit for understanding IP addresses and networks.

## 2 .Creating an IPv4 address

Use:

ipaddress.ip_address()

Example:

import ipaddress

ip = ipaddress.ip_address("192.168.1.10")

print(ip)
print(type(ip))

Output:

192.168.1.10
<class 'ipaddress.IPv4Address'>

Python automatically understands that this is IPv4.