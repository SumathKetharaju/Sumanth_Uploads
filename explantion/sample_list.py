input_list = [45, 87, 26, 31, 42, 12, 16, 85, 96]
max_element = input_list[0]
for item in input_list:
    if max_element < item:
        max_element = item
print(max_element)
