import re
input_date_of_birth = "29"

pattern = re.compile(r"^2[0-9]$")


match = pattern.search(input_date_of_birth)
# match = pattern.finditer(input_date_of_birth)
print(match)

if match:
    print("Valid date of birth")
else:
    print("Not a valid date of birth")