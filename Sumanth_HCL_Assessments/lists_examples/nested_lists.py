input_list = [[1, 2, 3, 2, 3], [56, -9, 47, 89], [14, 65, -47]]

single_list = []

for index in range(len(input_list)):
    for num in input_list[index]:
        single_list.append(num)

print(single_list)

final_list = [num for index in range(len(input_list)) for num in input_list[index] if num > 0]

print(final_list)

sample_list = [1, -2, 32, -96, 58, -78]
positive_numbers = []
for num in sample_list:
    # negative = num * -1
    if num > 0:
        positive_numbers.append(num)

print(positive_numbers)

positive_numbers_using_comprehension = [num for num in sample_list if num > 0]
print(positive_numbers_using_comprehension)



# list_1 = [1, 2, 3, 4, 2, 1, 3]
# duplicate_num = []
# for num in list_1:
#     for index in range(1, len(list_1)):
#         if num == list_1[index]:
#             duplicate_num.append(num)
#             list_1.remove(num)
#
# print(duplicate_num)

# input_list = [[1, 2, 3, 2, 3], [56, 89, 47, 89], [14, 65, 47]]
#
# single_list = []
#
# for index in range(len(input_list)):
#     for num in input_list[index]:
#         if num in index:
#             single_list.append(num)
#
# print(single_list)
#
# final_list = [num for index in range(len(input_list)) for num in input_list[index]]
#
# print(final_list)
# sample_list = [[[1, 3], [12, 3]], [[56, 89], [47, 56]], [[14, 65], [65, 49]]]
# sample_list = [[[1, 3], [12, 3]]]
# print(len(sample_list))
#
# unique_list = []
#
# for index in range(len(sample_list)):
#     for nested_index in range(len(sample_list[index])):
#         # for num in sample_list[nested_index]:
#         unique_list.append(sample_list[nested_index])
#
# print(unique_list)
# print(len(unique_list))
