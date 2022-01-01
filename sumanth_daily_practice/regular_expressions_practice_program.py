import re

input_string = input("Enter a string: ")

pattern = "^[+91]*[0-9]{10}$"

expected_output = re.match(pattern, input_string)

if expected_output:
    print("Valid mobile number")
else:
    print("Invalid mobile number")
