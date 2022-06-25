"""
Input ⇒ Welcome Yagna!  ,   given input string should be reversed, but the condition is that last
                            special character and space between the words should be in its
                            index position even after reversing the string
 this is the expected output
Output ⇒ angaYem ocleW!
"""
input_string = "Welcome Yagna!  ,"

special_char = "!@#$%^&*,. "

original_string = ""
rev_string = ""
rev_string_without_special_char = ""

len_of_input_string = len(input_string)
print(f"The length of the given input string is  --> {len_of_input_string}")
index_size_of_input_string = len(input_string) - 1
print(f"The index size of given input string is  --> {index_size_of_input_string}")
index_special_char = 0
index_of_char = 0

for index in range(len_of_input_string):
    original_string += input_string[index]
    if input_string[index] not in special_char:
        print(index_of_char)
        index_of_char = input_string.find(input_string[index])
        print(index_of_char)

        print(f"The charter at index numer {index} is --> {input_string[index]}")
        if input_string[index_size_of_input_string] not in special_char:
            rev_string_without_special_char += input_string[index_size_of_input_string]
            print(rev_string_without_special_char, "sumanth")
    else:
        print(index_special_char)
        index_special_char = input_string.find(input_string[index])
        print(index_special_char)
        print(f"The special charter at index numer {index} is --> {input_string[index]}")
        rev_string_without_special_char += input_string[index_special_char]
        print(rev_string_without_special_char)

    rev_string += input_string[index_size_of_input_string]
    index_size_of_input_string -= 1
print(f"Original is --> {original_string}")
print(f"Reversed is --> {rev_string}")
print(f"Reversed without special char is --> {rev_string_without_special_char}")

# for index in range(len_of_input_string):
#     if input_string[index_size_of_input_string] in special_char:
#         index_special_char = input_string.find(input_string[index_size_of_input_string])
#         # print(index_special_char)
#         if index_of_char != index_special_char:
#             print(index_special_char)
#             rev_string += "*"
#     else:
#         index_of_char = input_string.find(input_string[index])
#         if index_of_char != index_special_char:
#             rev_string += input_string[index_size_of_input_string]
#     index_size_of_input_string -= 1
#
# print(rev_string)

# for index in range(len_of_input_string):
#     # print(f"Character of given input string at index number {index} is --> {input_string[index]}")
#     if input_string[index] in special_char:
#         index_of_special_char = input_string.find(input_string[index])
#         if index_of_special_char == index:
#             rev_string += input_string[index]
#     else:
#         # rev_string += "s"
#         print(f"The Character of given input string at index number {index_size_of_input_string} is --> "
#               f"{input_string[index_size_of_input_string]}")
#         if input_string[index_size_of_input_string] not in special_char:
#             rev_string += input_string[index_size_of_input_string]
#             print(rev_string)
#         # print(f"The Character of given input string at index number after {index_size_of_input_string} is --> "
#         #       f"{input_string[index_size_of_input_string]}")
#     index_size_of_input_string -= 1
#
# print(rev_string)









# index = len(input_string) - 1
# print(index)
# for char in input_string:
#     print(char)
#     rev_string += char

# for index in range(len(input_string)-1, -1, -1):
#     if input_string[index] not in special_char:
#         rev_string += input_string[index]
#     else:
#         print(index)
#         # rev_string.replace(rev_string[index], input_string[index])
#         rev_string += input_string[index]
# print(rev_string)
