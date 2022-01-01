import re
# 9856234563
# +919856234563

input_string = input("Enter a number: ")

# pattern = re.compile(r"[0-9]{10}") #9856234563 Matched <re.Match object; span=(0, 10), match='9856234563'> valid
# pattern = re.compile(r"[0-9]{10}") #+919856234563 Matched <re.Match object; span=(1, 11),match='9198562345'>not valid

# pattern = re.compile(r"^[0-9]{10}$") # 9856234563 Matched <re.Match object; span=(0, 10), match='9856234563'> valid
# pattern = re.compile(r"^[0-9]{10}$") #+919856234563 not Matched None

# pattern = re.compile(r"^[+91]*[0-9]{10}$") #9856234563 Matched <re.Match object; span=(0, 10), match='9856234563'>
pattern = re.compile(r"^[+91]*[0-9]{10}$") #+919856234563 Matched <re.Match object; span=(0, 13), match='+919856234563'>
match = pattern.search(input_string)
print(match)

if match:
    print("Valid mobile number")
else:
    print("Not a valid mobile number")

