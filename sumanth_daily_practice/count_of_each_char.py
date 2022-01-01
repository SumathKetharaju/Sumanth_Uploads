input_string = input("Enter a string: ")

punctuations = " ,."

count = {}

for char in input_string:
    if char not in punctuations:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

print(count)


