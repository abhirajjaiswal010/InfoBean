import ipaddress

ip = ipaddress.ip_address("192.168.1.10")
ip = ipaddress.ip_address("2001:db8::1")

print(ip)
print(type(ip))