# This program tells about which port is closed and which port is opened
import nmap

# Here we are giving the ip address of the machine
ip_address = input("Enter valid ip address: ")

# Here we are giving the minimum port number
min_port = int(input("Enter minimum port number: "))

# Here we are giving the maximum port number
max_port = int(input("Enter maximum port number: "))

# Here we need to open port scanner
scanner = nmap.PortScanner()

for port in range(min_port, max_port+1):
    scan_machine = scanner.scan(ip_address, str(port))
    port_status = scan_machine["scan"][ip_address]["tcp"][port]["status"]
    print(f"{port} port status is {port_status}")
