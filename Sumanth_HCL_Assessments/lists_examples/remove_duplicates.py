sample_list = [12, 54, 63, 12, 58, 96, 24, 54, 36, 63, 12, 54, 12, 54, 89]

duplicate_indexes = []
# print(set(sample_list))
final_dict = {}

for index_1 in range(len(sample_list)):
    # print(f"------@@@@@@@@@@@@@-------{index_1} --> {sample_list[index_1]}-------------------------------")
    for index_2 in range(index_1+1, len(sample_list)):
        # print(f"-------------{index_2} --> {sample_list[index_2]}-------------------------------")
        if sample_list[index_1] == sample_list[index_2]:
            duplicate_indexes.append(index_2)
            # print(duplicate_indexes)
            # print(f"################## final --> {index_2} --> {sample_list[index_2]}----------------------------")
            if index_1 not in duplicate_indexes:
                # pass
                print(f"################## final --> {index_1} --> {sample_list[index_1]}---------------------------")
                print(f"################## final --> {index_2} --> {sample_list[index_2]}---------------------------")
                print(sample_list[index_2])
                final_dict[index_2] = sample_list[index_2]
                # sample_list.pop(index_2)


print(duplicate_indexes)
print(final_dict)

# sample_list = [12, 54, 63, 12, 58, 96, 24, 54, 36, 63, 12, 54, 12, 54, 89]
#
# len_of_sample_list = len(sample_list)
# duplicate_indexes = []
# # print(set(sample_list))
# final_dict = {}
#
# for num in sample_list:
#     index_of_num = sample_list.index(num)
#     print(f"------@@@@@@@@@@@@@-------{index_of_num} --> {sample_list[index_of_num]}-------------------------------")
#     print(len_of_sample_list)
#     for index_2 in range(index_of_num+1, len_of_sample_list):
#         print(len_of_sample_list)
#         print(f"-------^^^^^^^^------{index_2} --> {sample_list[index_2]}-------------------------------")
#         if num == sample_list[index_2]:
#             duplicate_indexes.append(index_2)
#             # print(duplicate_indexes)
#             print(f"################## final --> {index_2} --> {sample_list[index_2]}-------------------------------")
#             # sample_list.pop(index_2)
#             len_of_sample_list = len(sample_list)
#             print(sample_list)
#             print(len_of_sample_list)
            # if index_1 not in duplicate_indexes:
            #     # pass
            #     print(f"################## final --> {index_1} --> {sample_list[index_1]}---------------------------")
            #     print(f"################## final --> {index_2} --> {sample_list[index_2]}---------------------------")
            #     print(sample_list[index_2])
            #     final_dict[index_2] = sample_list[index_2]
                # sample_list.pop(index_2)


# print(duplicate_indexes)
# print(final_dict)
