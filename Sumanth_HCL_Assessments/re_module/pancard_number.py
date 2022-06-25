import re

"""
It should be ten characters long.
The first five characters should be any upper case alphabets.
The next four-characters should be any number from 0 to 9.
The last(tenth) character should be any upper case alphabet.
It should not contain any white spaces.
"""

# input_string = "ADWSD8965S"  # Given Pancard number 'ADWSD8965S' is valid
input_string = "BNZAA2318J"  # Given Pancard number 'BNZAA2318J' is valid
# input_string = "ODWSD8965R"  # Given Pancard number 'ODWSD8965R' is valid
# input_string = "23ZAABN18J"  # Given Pancard number is not valid
# input_string = "BNZAA2318JM"  # Given Pancard number is not valid
# input_string = "8ODWSD8965R" # Given Pancard number is not valid
# input_string = "O8DWSD8965R"  # Given Pancard number is not valid
# input_string = "ODWSD89965R"  # Given Pancard number is not valid
# input_string = "ODWSD89965R@"  # Given Pancard number is not valid

# pancard_pattern = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]$")
pancard_pattern = re.compile(r"^[A-Z]{5}\d{4}[A-Z]$")

pancard_match = pancard_pattern.search(input_string)

if pancard_match:
    print(pancard_match)
    print(f"Given Pancard number '{pancard_match.group()}' is valid")
else:
    print("Given Pancard number is not valid")
