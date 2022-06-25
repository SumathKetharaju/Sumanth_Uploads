import re

with open("all_data.txt", "r") as f:
    data = f.read()
    words = data.split()
    # print(words)
    for word in words:
        # pancard_pattern = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]$")
        pancard_pattern = re.compile(r"^[A-Z]{5}\d{4}[A-Z]$")
        pancard_match = pancard_pattern.search(word)
        if pancard_match:
            print(pancard_match.group())
