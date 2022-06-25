count_of_word = 0

count_of_each_word = {}

list_of_5_digit_words = []

with open("python_info.txt", "r") as f:
    data = f.read()
    list_of_words = data.split()
    for word in list_of_words:
        for char in word:
            # print(char)
            count_of_word += 1
            count_of_each_word[word] = count_of_word
        count_of_word = 0

# print(count_of_each_word)

for word, value in count_of_each_word.items():
    if value == 5:
        list_of_5_digit_words.append(word)

print(list_of_5_digit_words)

