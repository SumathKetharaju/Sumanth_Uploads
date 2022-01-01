import re

phone_number = input("Enter phone number: ")

pattern = "^[+91]*[0-9]{10}$"

result = re.search(pattern, phone_number)

if result:
    print("It is valid phone number")
else:
    print("It is not a valid phone number")
