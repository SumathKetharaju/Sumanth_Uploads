input_list = [12, 56, 98, 31, 24, 63, 26, 97, 47, 56, 99]
print(input_list)

reversed_list = []

print(input_list[::-1])

for index in range(len(input_list)-1, -1, -1):
    # print(input_list[index])
    reversed_list.append(input_list[index])

# print(reversed_list)

for num in input_list:
    index_of_num = input_list.index(num)
    if input_list[index_of_num] == reversed_list[index_of_num]:
        # print(index_of_num)
        # print(input_list[index_of_num])
        print(f"The common number at the same index after reversing the list is --> {input_list[index_of_num]} and its index is {index_of_num}")


        # index_of_num_2 = reversed_list.index(num)
        # if input_list[index_of_num] == reversed_list[index_of_num_2]:
        #     print(actual_num)

# for index_of_actual_num in range(len(input_list)):
#     if index_of_actual_num in
#     # for index_of_reversed_num in range(len(reversed_list)):
#     #     if input_list[index_of_actual_num] == reversed_list[index_of_reversed_num]:
#     #         print(input_list[index_of_actual_num])

