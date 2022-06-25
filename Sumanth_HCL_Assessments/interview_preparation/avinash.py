"""
Create a program that adds line numbers to a file. The name of the input file will be
read from the user, as will the name of the new file that your program will create.
Each line in the output file should begin with the line number, followed by a colon
and a space, followed by the line from the input file.
"""
data = "1, 2, 3, 4, 5, 6"
spli = data.splitlines()
print(spli)
with open("sample_file.txt", "w") as w:
    # print(line_number)
    w.write(str(1))

