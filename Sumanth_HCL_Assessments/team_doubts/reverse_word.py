input_string = "india is my country dad"

expected_output = ""

words = input_string.split()

# for word in words:
#     # print(word[::-1])
#     expected_output += word[::-1] + " "
#
# print(expected_output)

# for word in words:
#     for index in range(len(word)-1, -1, -1):
#         expected_output += word[index]
#     expected_output += " "
#
# print(expected_output)

for word in words:
    for index in range(len(word)-1, -1, -1):
        expected_output += word[index]
    print(expected_output)
    reversed_string = expected_output[:]
    if list(expected_output) == list(word):
        print(f"{expected_output} == {word} is a palindrome")
    # expected_output
    # expected_output += " "

print(expected_output)

