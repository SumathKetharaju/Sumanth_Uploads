input_list = ["India", "is", "my", "country", "and", "all", "indians"]
# Is@n@@s
index = 0
initial_item = input_list[0]
expected_string = ""

for item in input_list:
    len_of_initial_item = len(initial_item)
    if len(item) >= len_of_initial_item:
        expected_string += item[index]
        index += 1
    else:
        expected_string += "@"
        index += 1
print(expected_string)


