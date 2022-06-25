sample_string = "India is my country"
# {"India": 5, "is": 2, "my": 2, "country": 7}

expected_dict = {}

# for word in sample_string.split():
#     len_of_word = len(word)
#     expected_dict[word] = len_of_word
#
# print(expected_dict)

count_of_word = 0
for word in sample_string.split():
    for char in word:
        # print(char)
        count_of_word += 1
        expected_dict[word] = count_of_word
    count_of_word = 0

print(expected_dict)
