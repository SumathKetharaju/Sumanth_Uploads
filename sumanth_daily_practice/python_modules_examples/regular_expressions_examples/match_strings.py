import re

with open("matching_purpose.txt", "r") as m:
    data = m.read()
    pattern = re.compile(r"passed\b")
    match = pattern.search(data)
    print(match)
    if match:
        print(f"yes {match.group()} is present in the test file")
    else:
        print("fail")

# input_string = "sumanth sumanth sumanth mahesh raviteja 12"
#
# pattern = re.compile(r"\w+")
#
# match = pattern.search(input_string)
#
# # print(match.group())
#
# if match:
#     print(match.group())
# else:
#     print("fail")
