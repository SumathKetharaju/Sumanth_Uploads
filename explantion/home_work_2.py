"""
list_1 = [-1,2,3,-4,-5,-6,7,8,9,-10,11,-12,13]

dict_1 = {1: -1, 2: 4, 3: 27, 4: -4, 5: 25, 6: -216, 7: 7, 8: 64, 9: 729, 10: -10, 11: 121, 12: -1728, 13: 13}
"""
sample_list = [-1, 2, 3, -4, -5, -6, 7, 8, 9, -10, 11, -12, 13]
len_of_sample_list = len(sample_list)
final_output = {}
increment_num = 1
for actual_num in sample_list:
    if actual_num < 0:
        expected_num = actual_num ** increment_num
        positive_num = actual_num * -1
        final_output[positive_num] = expected_num
        increment_num += 1
        if increment_num > 3:
            increment_num = 1
    else:
        expected_num = actual_num ** increment_num
        final_output[actual_num] = expected_num
        increment_num += 1
        if increment_num > 3:
            increment_num = 1

print(final_output)
