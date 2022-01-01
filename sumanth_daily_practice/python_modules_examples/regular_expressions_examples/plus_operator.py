import re

input_sting = input("Enter a string: ")

pattern = "^b+s$"

result = re.search(pattern, input_sting)

if result:
    print("It is valid")
else:
    print("It is not valid")
