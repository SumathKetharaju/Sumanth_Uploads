input_dict = {"Sumanth": 1, "Ravindra": 2, "Sunil": 3, "Raja": 1, "Ramu": 2, "Ravi": 3}

# final_output = []
# first_rank_students = []
# second_rank_students = []
# third_rank_students = []
#
# for name, rank in input_dict.items():
#     if rank == 1:
#         first_rank_students.append(name)
#     elif rank == 2:
#         second_rank_students.append(name)
#     elif rank == 3:
#         third_rank_students.append(name)
# print(first_rank_students)
# print(second_rank_students)
# print(third_rank_students)


input_list = [["Sumanth", "Ravindra", "Sunil"], ["Raja", "Ramu", "Ravi"], ["Harish", "Mahesh", "Suresh"]]

final_output = []
first_rank_students = []
second_rank_students = []
third_rank_students = []

for index in range(len(input_list)):
    # print(len(input_list))
    # print(f"index  of that input list is --> {index}")
    # print(f"element  of that index of input list is --> {input_list[index]}")
    for nested_index in range(len(input_list[index])):
        # print(len(input_list[index]))
        # print(f"nested index  of that input list is --> {index}")
        # print(f"element of that nested index of input list is --> {input_list[index][nested_index]}")
        if nested_index == 0:
            first_rank_students.append(input_list[index][nested_index])
        elif nested_index == 1:
            second_rank_students.append(input_list[index][nested_index])
        elif nested_index == 2:
            third_rank_students.append(input_list[index][nested_index])

print(first_rank_students)
print(second_rank_students)
print(third_rank_students)
final_output.extend([first_rank_students, second_rank_students, third_rank_students])
print(final_output)

