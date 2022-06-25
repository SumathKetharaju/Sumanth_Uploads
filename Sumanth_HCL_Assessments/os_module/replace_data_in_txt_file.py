current_word = "Python"
replace_with = "Java"
with open("data.txt", "r") as f:
    data = f.read()
    # print(data)
    list_of_words = data.split()
    print(list_of_words)
    empty_string = ""
    for word in list_of_words:
        if word == current_word:
            word = word.replace(current_word, replace_with)
            empty_string += word + " "
        else:
            empty_string += word + " "
    with open("data.txt", "w") as w:
        w.write(empty_string)
        print(empty_string)

