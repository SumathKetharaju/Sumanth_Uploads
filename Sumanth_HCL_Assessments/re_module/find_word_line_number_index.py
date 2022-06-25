import re

with open("python.txt", "r") as f:
    data = f.read()
    print(f"-----------------------------The data Present in the 'python.txt' is ---------------------- \n\n{data}\n")
    list_of_each_line_data = data.splitlines()
    print(f"-----------------------------The list_of_each_line_data present in the 'python.txt' is --------------"
          f"-------- \n\n{list_of_each_line_data}\n")

    print(f"The total number of lines Present in 'python.txt' is --> {len(list_of_each_line_data)}\n")
    line_number = 0
    print(f"The initial Line number That we have taken is --> {line_number}\n")
    for line in list_of_each_line_data:
        list_of_each_word_in_line = line.split()
        # print(
        #     f"-----------------------------The list_of_each_word_in_line present in the 'python.txt' is --------------"
        #     f"-------- \n\n{list_of_each_word_in_line}\n")
        line_number += 1
        index_of_word = -1
        for word in list_of_each_word_in_line:
            python_word_pattern = re.compile(r"Python")
            python_word_match = python_word_pattern.search(word)
            index_of_word += 1
            if python_word_match:
                python = python_word_match.group()
                print(f"The word {python} is Present in line number {line_number} and "
                      f"it is placed in the index position --> {index_of_word} in that line only")


