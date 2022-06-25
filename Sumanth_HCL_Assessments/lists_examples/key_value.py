input_list = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

final_output = {}

for num in input_list:
    if num > 0:
        power_of_num = num ** 2
        final_output[num] = power_of_num
    else:
        positive_num = num * -1
        final_output[positive_num] = num

print(final_output)



