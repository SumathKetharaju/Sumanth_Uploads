sample_string = "hyderabadaeiou"

print(sample_string)

input_dict = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}

for char in sample_string:

    if char in input_dict:
        sample_string = sample_string.replace(char, str(input_dict[char]))

print(sample_string)

# for char, value in input_dict.items():
#     if char in sample_string:
#         sample_string = sample_string.replace(char, str(value))

# print(sample_string)
