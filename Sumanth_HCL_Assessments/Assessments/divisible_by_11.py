input_list = [12, 11, 26, 33, 110, 153, 121, 4563, 308, 132, 297, 209, 407, 418, 429, 528, 889, 605, 638]

zero_index = 0
first_index = 1
last_index = -1

for num in input_list:
    num_str = str(num)
    len_of_num_str = len(num_str)
    if len_of_num_str == 2:
        if num_str[zero_index] == num_str[last_index]:
            print(f"Given number {num_str} is divisible by 11, because 11 into {int(num_str) // 11} is {num_str}")
        else:
            print(f"Given number {num_str} is not divisible by 11, because 11 into {int(num_str) // 11} is not {num_str}")
    elif len_of_num_str == 3:
        if num_str[first_index] != "0" and num_str[first_index] != "1" and num_str[first_index] != "2":
            addition_of_zero_and_last = int(num_str[zero_index]) + int(num_str[last_index])
            if num_str[first_index] == str(addition_of_zero_and_last):
                print(f"Given number {num_str} is divisible by 11, because 11 into {int(num_str) // 11} is {num_str}")
            else:
                print(f"Given number {num_str} is not divisible by 11, because 11 into {int(num_str) // 11} is not {num_str}")

        else:
            print(f"Given number {num_str} is divisible by 11, because 11 into {int(num_str) // 11} is {num_str}")

    else:
        print(f"Please enter two digit number or three digit number")
else:
    print(f"All items are checked from ths list")
