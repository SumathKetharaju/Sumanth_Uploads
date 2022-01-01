import nmap

import re

ip_address_pattern = re.compile("^(?:[0-9]{1, 3}/.){3}[0-9]{1, 3}$")


port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0

port_max = 65535

open_ports = []

while True:
    ip_address_entered = input("Please enter the ip address that you want to scan: ")
    if ip_address_pattern.search(ip_address_entered):
        print(f"{ip_address_pattern} is a valid ip address")
        break

while True:
    print("Please enter the range of ports you want to scan in format: ")
    port_range = input("Enter port range")
    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()

for port in range(port_min, port_max):
    try:
        result = nm.scan(ip_address_entered, str(port))
        port_status = (result["scan"][ip_address_entered]["tcp"][port]["state"])
        print(f"Port {port} is {port_status}")
    except:
        print(f"Cannot scan port {port}")
