import re

"""
It should have 12 digits.
It should not start with 0 and 1.
It should not contain any alphabet and special characters.
It should have white space after every 4 digits.
"""
#
input_string = "5447 8154 9607"  # Given Aadhar number '5447 8154 9607' is valid
# input_string = "544781549607"  # Given Aadhar number is not valid
# input_string = "45447815496078"  # Given Aadhar number is not valid
# input_string = "0447 8154 9607"  # Given Aadhar number is not valid
# input_string = "1447 8154 9607"  # Given Aadhar number is not valid
# input_string = "5447 81549607"  # Given Aadhar number is not valid
# input_string = "54478154 9607"  # Given Aadhar number is not valid
# input_string = "A447 8B54 96C7"  # Given Aadhar number is not valid

# aadhar_pattern = re.compile(r"^[2-9]{4} [0-9]{4} [0-9]{4}$")
aadhar_pattern = re.compile(r"^[2-9]{4}\s[0-9]{4}\s[0-9]{4}$")
# aadhar_pattern = re.compile(r"^[2-9]{4} \d{4} \d{4}$")

aadhar_match = aadhar_pattern.search(input_string)

if aadhar_match:
    print(aadhar_match)
    print(f"Given Aadhar number '{aadhar_match.group()}' is valid")
else:
    print("Given Aadhar number is not valid")
