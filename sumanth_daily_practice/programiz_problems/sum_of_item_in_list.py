sample_list = [1, 2, 3]
sample_list_1 = ["Sumanth", "Ravindra", "Sasikanth", "praveen"]
expected_string = ""
index = 0
nested_index = 0
for item in sample_list_1:
    if index % 2 == 0:
        expected_string += item[nested_index]
        nested_index += 1
        index += 1
        if index > 1:
            index = 0
    else:
        len_of_item = len(item)
        expected_string += item[len_of_item-1]

print(expected_string)




expected_output = {}
for index in range(len(sample_list)):
    expected_output[sample_list[index]] = sample_list_1[index]

print(expected_output)
reversed_list = []
for index in range(len(sample_list)-1, -1, -1):
    reversed_list.append(sample_list[index])
print(reversed_list)


final_list = []
sum = 0
for item in sample_list:
    sum += item
print(sum)

for index in range(len(sample_list)):
    # print(f"index={index}")
    # print(f"len(sample_list) = {len(sample_list)}")
    for i in range(len(sample_list)//2):
        # print(f"index={index}")
        # print(f"len(sample_list) = {len(sample_list)}")
        # print(f"half_length = {len(sample_list) // 2}")
        # print(f"i = {i}")
        # print(f"len(sample_list)-i = {len(sample_list)-i}")
        if index != (len(sample_list)-i):
            if sample_list:
                first_index = sample_list[0]
                last_index = sample_list[-1]
                sum = first_index + last_index
                final_list.append(sum)
                sample_list.pop(0)
                sample_list.pop(-1)
print(f"final_list = {final_list}")

