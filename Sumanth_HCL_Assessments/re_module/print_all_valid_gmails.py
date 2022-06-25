import re

with open("all_data.txt", "r") as f:
    data = f.read()
    lines = data.splitlines()
    for line in lines:
        gmail_pattern = re.compile(r"^[A-Za-z][\w]+(\.|@|\$|-|_|~)*[\w+]*[@]+[a-z]{1,9}\.([a-z]{1,5}\.)*[a-z]{1,5}$")
        gmail_match = gmail_pattern.search(line)
        if gmail_match:
            print(gmail_match.group())
