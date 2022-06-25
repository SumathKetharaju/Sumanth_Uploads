current_word = "SBH"
replace_with = "SBI"
second_word = "Hyderabad"
replace_word = "India"
with open("employe_data.txt", "r") as f:
    data = f.read()
    # print(data)
    list_of_words = data.split()
    # print(list_of_words)
    final_string = ""
    count_of_word = 0
    for word in list_of_words:
        if word == current_word:
            count_of_word += 1
            word = word.replace(current_word, replace_with)
            final_string += word + " "
        elif word == second_word:
            word = word.replace(second_word, replace_word)
            final_string += word + " "
        else:
            final_string += word + " "
    print(count_of_word)
    with open("employe_data.txt", "w") as w:
        w.write(final_string)
        print(final_string)

