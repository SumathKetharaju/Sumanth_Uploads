input_tuple = (2, 4, 3, 8, 5, 15)
#
# for num in input_tuple:
#     for index in range(1, len(input_tuple)):
#         num *= input_tuple[index]
#     print(num)
#     break
#
first_num = input_tuple[0]
for index in range(1, len(input_tuple)):
    first_num *= input_tuple[index]
print(first_num)
#

initial_num = input_tuple[0]
for index in range(1, len(input_tuple)):
    initial_num += input_tuple[index]
print(initial_num)

# sample_tuple = ((2, 3), (4, 5), (6, 7), (2, 8))
sample_tuple = ((2, 3, 5), (4, 5, 6), (6, 7, 8), (2, 8, 9))
#
expected_list_multiplication_numbers = []

for index in range(len(sample_tuple)):
    first_num = sample_tuple[index][0]
    for nested_index in range(1, len(sample_tuple[index])):
        # print(len(sample_tuple[index]))
        # first_num = sample_tuple[index][0]
        # print(first_num)
        # print(sample_tuple[index][nested_index])
        first_num *= sample_tuple[index][nested_index]
    # print(first_num)
    expected_list_multiplication_numbers.append(first_num)

print(expected_list_multiplication_numbers)

expected_list_addition_numbers = []
for index in range(len(sample_tuple)):
    first_num = sample_tuple[index][0]
    for nested_index in range(1, len(sample_tuple[index])):
        # print(len(sample_tuple[index]))
        # first_num = sample_tuple[index][0]
        # print(first_num)
        # print(sample_tuple[index][nested_index])
        first_num += sample_tuple[index][nested_index]
    # print(first_num)
    expected_list_addition_numbers.append(first_num)

print(expected_list_addition_numbers)

# for index in range(len(sample_tuple)):
#     first_num = sample_tuple[index][0]
#     for nested_index in range(1, len(sample_tuple[index])):
#         # print(len(input_list[index]))
#         first_num = sample_tuple[index][0]
#         # print(first_num)
#         print(sample_tuple[index][nested_index])
#         first_num *= sample_tuple[index][nested_index]
#         expected_list.append(first_num)
#
# print(expected_list)


