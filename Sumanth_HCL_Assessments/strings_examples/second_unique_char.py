input_string = "This is a !@#$%^&* .>,<?:;/+|{[}] Pycharm IDE"

special_characters = "!@#$%^&* .>,<?:;/+|{[}]"

count_of_char = {}

for char in input_string:
    if char not in special_characters:
        if char not in count_of_char:
            count_of_char[char] = 1
        else:
            count_of_char[char] += 1

print(f"Count of each character is --> {count_of_char}")

for char, value in count_of_char.items():
    if value > 1:
        print(f"The Duplicate character from the given string is --> {char} and it Position is --> {input_string.index(char)}")
        break

