import re

print(f"\n------------------- Vowels replacement using regular expression findall and sub method--------------------\n")

sample_string = "hyderabadaeiou"
print(f"Given Sample String is --> {sample_string}")

reference_string = sample_string
print(f"Reference String is --> {reference_string}")

vowel_pattern = r"[aeiou]"
input_dict = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}

vowels_match = re.findall(vowel_pattern, reference_string)
print(f"The vowels which are present in the reference string is --> {vowels_match}")

replaced_string = ""

for char in sample_string:
    if char in vowels_match:
        replaced_string = re.sub(char, str(input_dict[char]), reference_string)
        reference_string = replaced_string

print(f"The string after replacing vowels with numbers is --> {replaced_string}")
print(f"Given Sample String after replacing vowels with numbers is --> {sample_string}")
print(f"Reference String after replacing vowels with numbers is --> {reference_string}\n")

print(f"------------------------ Vowels replacement without using regular expression -------------------------------\n")

input_string = "hyderabadaeiou"
print(f"Given input String is --> {input_string}")

duplicate_string = input_string
print(f"Duplicate String is --> {duplicate_string}")

input_dict = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}

for char in sample_string:
    if char in input_dict:
        duplicate_string = duplicate_string.replace(char, str(input_dict[char]))

print(f"Duplicate String after replacing vowels with numbers is --> {duplicate_string}")
print(f"Given input String after replacing vowels with numbers is --> {input_string}")

print(f"\n------------------- Vowels replacement using regular expression findall and subn method-------------------\n")

print(f"TypeError: expected string or bytes-like object")

# given_string = "hyderabadaeiou"
# print(f"Given String is --> {given_string}")
#
# ref_string = sample_string
# print(f"Reference String is --> {ref_string}")
#
# vl_pattern = r"[aeiou]"
# sample_dict = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
#
# vl_match = re.findall(vl_pattern, ref_string)
# print(f"The vowels which are present in the reference string is --> {vl_match}")
#
# replace_string = ""
#
# for char in given_string:
#     if char in vl_match:
#         # TypeError: expected string or bytes-like object
#         replace_string = re.subn(char, str(sample_dict[char]), ref_string)
#         ref_string = replace_string
#
# print(f"The string after replacing vowels with numbers is --> {replace_string}")
# print(f"Given Sample String after replacing vowels with numbers is --> {given_string}")
# print(f"Reference String after replacing vowels with numbers is --> {ref_string}\n")

