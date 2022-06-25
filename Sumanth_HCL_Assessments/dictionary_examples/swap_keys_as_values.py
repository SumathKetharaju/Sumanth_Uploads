input_dict = {1: 2, 2: 4, 3: 6, 4: 8}

# sample_dict = {}
#
# for key, value in input_dict.items():
#
#     sample_dict[value] = key
#
# print(sample_dict)

sample_dict = {23: "Sumanth", "Ravindra": 24, 20: "Sudheer", "Sunil": 22}

final_dict = {}

for key, value in sample_dict.items():
    if type(key) != str:
        final_dict[value] = key
    else:
        final_dict[key] = value
print(final_dict)

dict_comprehension = {key if type(key) != str else "s" for key, value in sample_dict.items()}

print(dict_comprehension)
