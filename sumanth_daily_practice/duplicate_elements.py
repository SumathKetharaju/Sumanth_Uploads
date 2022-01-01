input_list = [12, 54, 32, 12, 49, 87, 63, 54, 12, 54, 87]

duplicates = {}

for item in input_list:
    if item not in duplicates:
        duplicates[item] = 1
    else:
        duplicates[item] += 1
        if duplicates[item] == 2:
            print(item)

# print(duplicate_elements)
for key, value in duplicates.items():
    if value > 1:
        print(key)

