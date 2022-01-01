input_string = input("Enter a string: ")

punctuations = " ,."

count = {}

second_time_count = 0

for char in input_string:
    if char not in punctuations:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
            second_time_count += 1
            if second_time_count == 2:
                print(char)
                # break
