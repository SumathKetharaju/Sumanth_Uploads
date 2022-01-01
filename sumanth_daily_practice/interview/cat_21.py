import re
input_string = "H@#$#$%#@ello@#!!123World"
# output = Hello123world

special_characters = "#$%@!*()+-"
expected_string = ""

for char in input_string:
    if char not in special_characters:
        expected_string += char

print(expected_string)

pattern = re.compile(r"[\w]")

matches = pattern.finditer(input_string)

for match in matches:
    print(match.group(), end="")

