import re


with open("all_data.txt", "r") as f:
    data = f.read()
    lines = data.splitlines()
    # print(words)
    for line in lines:
        # aadhar_pattern = re.compile(r"^[2-9]{4} [0-9]{4} [0-9]{4}$")
        aadhar_pattern = re.compile(r"^[2-9]{4} [0-9]{4} [0-9]{4}$")
        aadhar_match = aadhar_pattern.search(line)
        if aadhar_match:
            print(aadhar_match.group())
