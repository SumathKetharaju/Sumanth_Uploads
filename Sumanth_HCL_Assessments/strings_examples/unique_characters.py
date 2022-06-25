#  write a code to print that first unique character and position of that character

# input_string = "fgyytuuugg"
input_string = "This is a T Pycharm IDE !@#$%^&* .>,<?:;/+|{[}]"

special_characters = "!@#$%^&* .>,<?:;/+|{[}]"

count_of_char = {}

unique = []
duplicate = []

for char in input_string:
    if char not in special_characters:
        if input_string.count(char) == 1:
            unique.append(char)
        else:
            duplicate.append(char)

print(unique[0])
print(input_string.index(unique[0]))

print(count_of_char)


for char in input_string:
    if char not in special_characters:
        if char not in count_of_char:
            count_of_char[char] = 1
        else:
            count_of_char[char] += 1
print(count_of_char)

for char, value in count_of_char.items():
    if value == 1:
        print(char)
        print(input_string.index(char))
        break


# for char in input_string:
#     if char not in special_characters:
#         if char not in count_of_char:
#             count_of_char[char] = 1
#         else:
#             count_of_char[char] += 1
#             print(char)
#             print(input_string.index(char))
#             print(f"The first unique character of the given string is --> {char} and its index is {input_string.index(char)}")
#             print(f"The first unique character of the given string is --> {char} and its index is {input_string.find(char)}")
#             break


# print(count_of_char)
# for index in range(len(input_string)):
#     for nested_index in range(index+1, len(input_string)):
#         if input_string[index] == input_string[nested_index]:
#             print(input_string[index])
