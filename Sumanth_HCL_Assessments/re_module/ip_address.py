import re

# input_ip = "192.156.253.624"

"""
192.0.2.0 - 192.0.2.255.
198.51.100.0 - 198.51.100.255.
203.0.113.0 - 203.0.113.255.

"""
# input_ip = "192.168.1.1.1"
# input_ip = "192.0.2.0"
# input_ip = "192.0.2.255"
# input_ip = "198.51.100.0"
input_ip = "198.51.100.255"
# input_ip = "203.0.113.0"
# input_ip = "203.0.113.255"
# input_ip = "255.255.255.255"

# ip_pattern = re.compile(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$")
"""
Any one- or two-digit number.
Any three-digit number beginning with 1 .
Any three-digit number beginning with 2 if the second digit is 0 to 4 .
Any three-digit number beginning with 25 if the third digit is 0 to 5 .
"""
ip_pattern = re.compile(r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b')

ip_match = ip_pattern.search(input_ip)

if ip_match:
    print(f"Given {input_ip} is matched")
    print(ip_match)
    print(ip_match.group())
else:
    print(f"Given {input_ip} is not matched")

