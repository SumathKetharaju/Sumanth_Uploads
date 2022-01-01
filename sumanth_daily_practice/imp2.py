import re
input_string = "rajaram"
pattern = "^r.....m$"
result = re.search(pattern, input_string)
if result:
    print("Success")
else:
    print("Not success")
for char in input_string:
    if char == "a":
        print("a")
