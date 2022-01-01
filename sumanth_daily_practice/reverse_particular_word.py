# sumanth raveendra sumanth raveendra sudheer
input_string = input("Enter a string: ")

splitted_string = input_string.split()

for word in splitted_string:
    if "n" in word:
        index = word.find("n")
        # print(word, index)
        if index % 2 != 0:
            print(word[::-1], end=" ")
        else:
            print(word, end=" ")
    else:
        print(word, end=" ")

