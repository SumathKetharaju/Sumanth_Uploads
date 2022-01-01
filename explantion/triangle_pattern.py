"""
*
**
***
****
*****
"""
# rows = 5
# for r in range(0, rows):
#     for c in range(0, r+1):
#         print("*", end="")
#     print()


"""
*****
****
***
**
*
"""
# rows = 5
# columns = 5
# for r in range(0, rows):
#     for c in range(columns, 0, -1):
#         print("*", end="")
#     columns -= 1
#     print()

# rows = 5
# for r in range(rows, 0, -1):
#     for c in range(0, r):
#         print("*", end="")
#     print()

# i = 1
# while i <= 5:
#     print(f"{'*'* i}")
#     i += 1
# print()

# i = 5
# while i != 0:
#     print(f"{'*'* i}")
#     i -= 1


"""
list_1 = [-1,2,3,-4,-5,-6,7,8,9,-10,11,-12,13]

if value is -1 , make it postive for key

dict_1 = {1:-1,2:4,3:9,4:-4,5:25,6:-216}
"""

# sample_list = [-1, 2, 3, -4, -5, -6, 7, 8, 9, -10, 11, -12, 13]
#
# dict_1 = {1: -1, 2: 4, 3: 9, 4: -4, 5: 25, 6: -6}
#
# final_dict = {}
#
# for actual_num in sample_list:
#     if actual_num < 0:
#         convert_negative_num_positive_num = actual_num * -1
#         positive_num = convert_negative_num_positive_num
#         final_dict[positive_num] = actual_num
#     else:
#         power_of_num = actual_num * actual_num
#         final_dict[actual_num] = power_of_num
# print(final_dict)

# rows = 5
# space = rows-1
# for r in range(0, rows):
#     for c in range(0, space):
#         print(end=" ")
#     space = space - 1
#     for c in range(0, r+1):
#         print("*", end=" ")
#     print()

rows = 7
space = rows-1
for r in range(0, rows):
    if r % 2 == 0:
        for c in range(0, space):
            print(end=" ")
        space = space - 2
        for c in range(0, r+1):
            print("*", end=" ")
        print()
