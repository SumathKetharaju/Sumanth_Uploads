"""
list_1 = [-1,2,3,-4,-5,-6,7,8,9,-10,11,-12,13]

if num is positive then make it as double and placed it as a value for that num{2:4}
if num is negative then make it as positive and placed it as a key for that num{1:-1}

dict_1 = {1: -1, 2: 4, 3: 9, 4: -4, 5: -5, 6: -6, 7: 49, 8: 64, 9: 81, 10: -10, 11: 121, 12: -12, 13: 169}

"""
#
# sample_list = [-1, 2, 3, -4, -5, -6, 7, 8, 9, -10, 11, -12, 13]
# final_output = {}
# for actual_num in sample_list:
#     if actual_num < 0:
#         convert_negative_num_positive = actual_num * -1
#         positive_num = convert_negative_num_positive
#         final_output[positive_num] = actual_num
#     else:
#         power_of_num = actual_num ** 2
#         final_output[actual_num] = power_of_num
#
# print(final_output)

"""
*
**
***
****
*****
"""

# for row in range(0, 5):
#     if row % 2 != 0:
#         for column in range(0, row+1):
#             print("*", end="")
#         print()

""" How to print a char which is existing in two times in a string"""
# sample_string = "sumanths"
# count = {}
# for char in sample_string:
#     if char not in count:
#         count[char] = 1
#     else:
#         count[char] += 1
#         print(char)


"""
*****
****
***
**
*
"""
for row in range(5, 0, -1):
    for column in range(row):
        print("*", end="")
    print()


