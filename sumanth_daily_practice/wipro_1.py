input_list = [12, 84, 57, 96, 14, 23, 65, 45, 87, 46]

maximum_item_in_list = []

for item in input_list:
    maximum_item = input_list[0]
    if item > maximum_item:
        maximum_item_in_list.append(item)
        input_list.remove(item)
print(maximum_item_in_list)

