input_list = [12, 89, 63, 54, 1278, 69, 586, 158, 627, 987]

max_num = input_list[0]

second_max_num = 0

for num in input_list:
    if max_num < num:
        max_num = num
    if second_max_num < num < max_num:
        second_max_num = num

print(max_num)
print(second_max_num)
