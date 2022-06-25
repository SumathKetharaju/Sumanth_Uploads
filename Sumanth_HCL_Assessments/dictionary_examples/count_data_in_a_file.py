input_string = "THis is SumaNth MOBILE numBer 6300905711 his password is 612"

count_of_each_digit = {}
digits_count = 0
count_of_lower_case_char = {}
lower_case_chars_count = 0
count_of_upper_case_char = {}
upper_case_chars_count = 0

for char in input_string:
    if char.isdigit():
        if char not in count_of_each_digit:
            count_of_each_digit[char] = 1
        else:
            count_of_each_digit[char] += 1

        digits_count += 1

    if char.islower():
        if char not in count_of_lower_case_char:
            count_of_lower_case_char[char] = 1
        else:
            count_of_lower_case_char[char] += 1

        lower_case_chars_count += 1

    if char.isupper():
        if char not in count_of_upper_case_char:
            count_of_upper_case_char[char] = 1
        else:
            count_of_upper_case_char[char] += 1

        upper_case_chars_count += 1

print("-----------------------------------------Digits ---------------------------------------------------------")
print(f"Total digits in the given string is --> {digits_count}")
print(f"Count of each digit in the given string is --> {count_of_each_digit}")

print("-----------------------------------------lower case characters ------------------------------------------------")
print(f"Total lowercase characters in the given string is --> {lower_case_chars_count}")
print(f"Count of each lowercase character in the given string is --> {count_of_lower_case_char}")

print("-----------------------------------------upper case characters ------------------------------------------------")
print(f"Total uppercase characters in the given string is --> {upper_case_chars_count}")
print(f"Count of each uppercase character in the given string is --> {count_of_upper_case_char}")

# dict_char = {}
# space = " .'/"
# with open("data.txt", "r") as f:
#     data = f.read()
#     print(len(data))
#     for char in data:
#         if char not in dict_char:
#             if char not in space:
#                 dict_char[char] = 1
#         else:
#             dict_char[char] += 1
#
# print(dict_char)
