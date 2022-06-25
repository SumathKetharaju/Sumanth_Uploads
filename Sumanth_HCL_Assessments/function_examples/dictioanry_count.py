import re


def count_of_each_characters(data_type):

    if type(data_type) == list or type(data_type) == tuple:
        count_of_num = {}
        for num in data_type:
            if num not in count_of_num:
                count_of_num[num] = 1
            else:
                count_of_num[num] += 1
        print(f"Count of each numbers is --> {count_of_num}")
        return f"Count of each numbers is --> {count_of_num}"
    elif type(data_type) == str:
        count_of_char = {}
        alpha_special_char = re.compile(r"([@\$#%\^\*\+\.!%&])")
        alpha_special_char_match = alpha_special_char.findall(data_type)
        alpha_special_word = re.compile(r"[@\$#%\^\*\+\.!%&]+")
        alpha_special_word_match = alpha_special_word.findall(data_type)
        space = " "
        converted_to_list = list(data_type)
        splitted_string = data_type.split()
        if space not in data_type:
            print(f"converted_to_list is --> {converted_to_list}")
            print(alpha_special_char_match)
            for char in converted_to_list:
                if char not in alpha_special_char_match:
                    if char != space:
                        if char not in count_of_char:
                            count_of_char[char] = 1
                        else:
                            count_of_char[char] += 1
            print(f"Count of Each characters are --> {count_of_char}")
        else:
            count_of_word = {}
            print(f"Splitted string is --> {splitted_string}")
            print(alpha_special_word_match)
            for word in splitted_string:
                if word not in alpha_special_word_match:
                    if word != space:
                        if word not in count_of_word:
                            count_of_word[word] = 1
                        else:
                            count_of_word[word] += 1
            print(f"Count of Each word is --> {count_of_word}")
    else:
        print(f"your entered incorrect data that is in format of {type(data_type)}, So please enter valid list or tuple or string")


input_list = [14, 53, 26, 89, 14, 23, 53, 67]
input_tuple = (14, 53, 26, 89, 14, 23, 53, 67)
input_string = "SumanthHarsish!##%$$^!%^"
sample_string = "Harish Sumanth Pycha#rm @#@#$# Sumanth"
count_of_each_characters(input_list)
count_of_each_characters(input_tuple)
count_of_each_characters(input_string)
count_of_each_characters(sample_string)


