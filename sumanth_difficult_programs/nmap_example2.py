import nmap

ip_address = input("Enter valid ip address you want to scan: ")

port_min = int(input("Enter minimum port number: "))

port_max = int(input("Enter maximum port number"))

scanner = nmap.PortScanner()

for port in range(port_min, port_max+1):
    result = scanner.scan(ip_address, str(port))
    port_status = result["scan"][ip_address]["tcp"][port]["state"]
    print(f"port {port} is {port_status}")
