import nmap

ip_address = input("Enter Valid Ip address: ")

min_port = int(input("Enter minimum port number: "))
max_port = int(input("Enter maximum port number: "))

scanner = nmap.PortScanner()

for port in range(min_port, max_port+1):
    result = scanner.scan(ip_address, str(port))
    port_status = result["scan"][ip_address]["tcp"][port]["status"]
    print(f"{port} port status is {port_status}")
