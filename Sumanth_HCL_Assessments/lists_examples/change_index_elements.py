input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

final_output = []
nested_zero_index_elements = []
nested_first_index_elements = []
nested_second_index_elements = []

for index in range(len(input_list)):
    # print(len(input_list))
    # print(f"index  of that input list is --> {index}")
    # print(f"element  of that index of input list is --> {input_list[index]}")
    for nested_index in range(len(input_list[index])):
        # print(len(input_list[index]))
        # print(f"nested index  of that input list is --> {index}")
        # print(f"element of that nested index of input list is --> {input_list[index][nested_index]}")
        if nested_index == 0:
            nested_zero_index_elements.append(input_list[index][nested_index])
        elif nested_index == 1:
            nested_first_index_elements.append(input_list[index][nested_index])
        elif nested_index == 2:
            nested_second_index_elements.append(input_list[index][nested_index])

# print(nested_zero_index_elements)
# print(nested_first_index_elements)
# print(nested_second_index_elements)
final_output.extend([nested_zero_index_elements, nested_first_index_elements, nested_second_index_elements])
print(final_output)

