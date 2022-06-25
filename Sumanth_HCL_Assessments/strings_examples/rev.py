from string import punctuation
special_char = "!@#$%^&* .,;:"
# input_string = "String; 2be reversed..."
input_string = "Welcome Yagna!  ,"
splitted_string = input_string.split()
reversed_words = []
for word in splitted_string:
    list_of_chars = [char for char in word if char not in special_char]
    print(list_of_chars)
    for char in word:
        if char not in special_char:
            # print(list_of_chars.pop())
            reversed_words.append(list_of_chars.pop())
            # print(reversed_words)
            continue
        else:
            reversed_words.append(char)
    reversed_words.append(' ')
print("".join(reversed_words))
