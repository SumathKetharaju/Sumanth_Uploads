import re

sample_string = "hyderabadaeiou"

print(sample_string)

input_dict = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}

vowels_match = re.findall(r"[aeiou]", sample_string)
print(vowels_match)
replace_string = ""
for char in sample_string:
    if char in vowels_match:
        replace_string = re.sub(char, str(input_dict[char]), sample_string)
        sample_string = replace_string
# print(sample_string)
print(replace_string)


# for char in sample_string:
#     vowels_pattern = re.compile("[aeiou]")
#     vowels_match = vowels_pattern.search(char)
#     if vowels_match:
#         vowel = vowels_match.group()
#         # print(vowel)
#         if vowel in input_dict:
#             sample_string = sample_string.replace(vowel, str(input_dict[vowel]))
#
# print(sample_string)

















# for char in sample_string:
#     vowels_pattern = re.compile("[aeiou]")
#     vowels_match = vowels_pattern.search(char)
#     if vowels_match:
#         vowel = vowels_match.group()
#         # print(vowels)
#         if vowel == "a":
#             replace_string_with_1 = sample_string.replace(vowel, "1")
#             sample_string = replace_string_with_1
#             # print(replace_string_with_1)
#
#         elif vowel == "e":
#             replace_string_with_2 = sample_string.replace(vowel, "2")
#             sample_string = replace_string_with_2
#             # print(replace_string_with_2)
#
#         elif vowel == "i":
#             replace_string_with_3 = sample_string.replace(vowel, "3")
#             sample_string = replace_string_with_3
#             # print(replace_string_with_3)
#
#         elif vowel == "o":
#             replace_string_with_4 = sample_string.replace(vowel, "4")
#             sample_string = replace_string_with_4
#             # print(replace_string_with_4)
#
#         elif vowel == "u":
#             replace_string_with_5 = sample_string.replace(vowel, "5")
#             sample_string = replace_string_with_5
#             # print(replace_string_with_5)
#
#         else:
#             pass
# print(sample_string)
