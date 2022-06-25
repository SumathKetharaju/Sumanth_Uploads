import re


def min_num(iterable):

    if type(iterable) == list or type(iterable) == tuple or type(iterable) == set:

        minimum_num = 1000

        for num in iterable:
            num = int(num)
            if num < minimum_num:
                minimum_num = num
        print(f"The Minimum number from the given {type(iterable)} is --> {minimum_num}")

    elif type(iterable) == str:
        alpha_special_word = re.compile(r"([A-Za-z]+|[@\$#%\^\*\+\.!%&]+)")
        alpha_special_word_match = alpha_special_word.findall(iterable)
        alpha_special_char = re.compile(r"([A-Za-z]|[@\$#%\^\*\+\.!%&])")
        alpha_special_char_match = alpha_special_char.findall(iterable)
        space = " "
        converted_to_list = list(iterable)
        splitted_string = iterable.split()
        min_number = 1000000000
        if space not in iterable:
            print(converted_to_list)
            print(alpha_special_char_match)
            for num in converted_to_list:
                if num not in alpha_special_word_match and num not in alpha_special_char_match:
                    num = int(num)
                    if num < min_number:
                        min_number = num
        else:
            print(splitted_string)
            print(alpha_special_word_match)
            for num in splitted_string:
                if num not in alpha_special_word_match and num not in alpha_special_char_match:
                    num = int(num)
                    if num < min_number:
                        min_number = num

        print(f"The Minimum number from the given {type(iterable)} is --> {min_number}")

    else:
        print(f"your entered incorrect data that is in format of {type(iterable)}, So please enter valid list or tuple or set or string")


input_list = [12, 65, 32, 45, 894, 457, 265]
input_set = {2, 65, 32, 45, 894, 1457, 265}
input_tuple = (12, 5, 32, 45, 894, 1457, 2265)
input_string = "25 56 6 896 Sumanth @$#$#%$#$@!@#$%^&"
sample_string = "239648uyfgry!@#$"
input_dict = {"name": 23, "Harish": 25}


min_num(input_list)
min_num(input_set)
min_num(input_tuple)
min_num(input_string)
min_num(sample_string)
min_num(input_dict)
print(min(input_set))
print(min(input_list))
print(min(input_tuple))
print(min(input_string))
print(min(sample_string))
print(min(input_dict.values()))



