import re


def max_num(iterable):

    if type(iterable) == list or type(iterable) == tuple or type(iterable) == set:
        maximum_num = 0
        for num in iterable:
            num = int(num)
            if num > maximum_num:
                maximum_num = num
        print(f"The Maximum number from the given {type(iterable)} is --> {maximum_num}")

    elif type(iterable) == str:
        alpha_special_word = re.compile(r"([A-Za-z]+|[@\$#%\^\*\+\.!%&]+)")
        alpha_special_word_match = alpha_special_word.findall(iterable)
        alpha_special_char = re.compile(r"([A-Za-z]|[@\$#%\^\*\+\.!%&])")
        alpha_special_char_match = alpha_special_char.findall(iterable)
        space = " "
        converted_to_list = list(iterable)
        splitted_string = iterable.split()
        max_number = 0
        if space not in iterable:
            print(converted_to_list)
            print(alpha_special_char_match)
            for num in converted_to_list:
                if num not in alpha_special_word_match and num not in alpha_special_char_match:
                    num = int(num)
                    if num > max_number:
                        max_number = num
        else:
            print(splitted_string)
            print(alpha_special_word_match)
            for num in splitted_string:
                if num not in alpha_special_word_match and num not in alpha_special_char_match:
                    num = int(num)
                    if num > max_number:
                        max_number = num

        print(f"The Maximum number from the given {type(iterable)} is --> {max_number}")

    else:
        print(f"your entered incorrect data that is in format of {type(iterable)}, So please enter valid list or tuple or set or string")


input_list = [12, 65, 32, 45, 894, 457, 265, "5688"]
input_set = {12, 65, 32, 45, 894, 457, 265, "986"}
input_tuple = (12, 65, 32, 45, 89.4, 145.7, 226.5)
input_string = "25 56 6 896 sumanth"
sample_string = "239648iuhdus"
input_dict = {"name": 23, "Harish": 25}

max_num((25, 26))
max_num(input_list)
max_num(input_set)
max_num(input_tuple)
max_num(input_string)
max_num(sample_string)
max_num(input_dict)
max_num("56 89")
# print(max(input_set))
# print(max(input_list))
print(max(input_tuple))
print(max(input_string))
print(max(input_dict.values()))

