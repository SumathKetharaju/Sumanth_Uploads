import re

"""
It should have in the format of date-month-year.
here date will between 1 to 31.
and month will between 1 to 12.
and year will between 1 to 12.
It should not contain any alphabet and special characters.
It should have white space after every 4 digits.
"""

# input_date_of_birth = "11-12-1998" # pass
# input_date_of_birth = "36/6/1998" #it should fail
# input_date_of_birth = "0-1-2022" #it should fail
# input_date_of_birth = "28/6/1998" #pass
# input_date_of_birth = "11/0/1998" #it should fail
# input_date_of_birth = "11/13/1998" #it should fail
# input_date_of_birth = "11@06@1998" #it should fail
# input_date_of_birth = "1-1-2022" #pass
input_date_of_birth = "31-1-1" #fail

date_of_birth_pattern = re.compile(r"^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(-|/)([1-9]|0[1-9]|1[0-2])(-|/)\d{1,4}$")
# date_of_birth_pattern = re.compile(r"^[2-9]{4} \d{4} \d{4}$")

date_of_birth_match = date_of_birth_pattern.search(input_date_of_birth)

if date_of_birth_match:
    print(date_of_birth_match)
    print(f"Given Date of birth '{date_of_birth_match.group()}' is valid")
else:
    print("Given Date of birth is not valid")



