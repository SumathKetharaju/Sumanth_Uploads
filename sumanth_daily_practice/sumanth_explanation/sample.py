sample_list_1 = [2, 3, 4, 5, 6, 3, 7, 8, 9, 10]
sample_list = [12, 13, 58, 96, 47, 54, 72, 15, 42, 18]

# for index in range(len(sample_list)):
#     if sample_list[index+1] < sample_list[index]:
#         print(sample_list[index+1])
#         break
expected_list_1 = []
expected_list_2 = []
for index in range(len(sample_list)):
    for index_2 in range(index+1, len(sample_list)):
        if sample_list[index] > sample_list[index_2]:
            expected_list_1.append(sample_list[index])
        else:
            expected_list_2.append(sample_list[index])
        sample_list.append(sample_list[index])
        sample_list.remove(sample_list[index])

print(expected_list_1)
print(expected_list_2)

final_list = []
while sample_list:
    pass








