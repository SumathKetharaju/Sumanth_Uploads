import re


with open("all_data.txt", "r") as f:
    data = f.read()
    words = data.split()
    # print(words)
    for word in words:
        date_of_birth_pattern = re.compile(r"^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(-|/)([1-9]|0[1-9]|1[0-2])(-|/)\d{1,4}$")
        date_of_birth_match = date_of_birth_pattern.search(word)
        if date_of_birth_match:
            print(date_of_birth_match.group())

