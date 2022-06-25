input_list = [85, 96, 35, 98, 74, 61, 32]

expected_list = []

length_input_list = 0

for item in input_list:
    length_input_list += 1

zero_index = 0
len_of_input_list = len(input_list)
last_index = len_of_input_list - 1

for index in range(length_input_list):
    if index == zero_index:
        input_list.insert(last_index, input_list[index])
        input_list.pop(index)
    elif index == last_index:
        input_list.insert(zero_index, input_list[index])
        input_list.pop(last_index + 1)

print(input_list)
