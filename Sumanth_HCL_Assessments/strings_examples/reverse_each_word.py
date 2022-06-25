reversed_string = ""

with open("python_info.txt", "r") as f:
    data = f.read()
    list_of_words = data.split()

    for word in list_of_words:
        for index in range(len(word)-1, -1, -1):
            reversed_string += word[index]
        reversed_string += " "
    # print(reversed_words)
    list_of_reversed_words = reversed_string.split()
    # print(reversed_strings_list)
    for actual_word in list_of_words:
        for reversed_word in list_of_reversed_words:
            if actual_word == reversed_word:
                print(f"actual_word({actual_word}) == reversed_word({reversed_word}), So the given word is palindrome")

    # reversed_strings_list.append(reversed_string)
