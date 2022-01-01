list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 4, 5]

final_list = []

for item in list_1:
    if item in list_2:
        sum = item + item
        final_list.append(sum)

print(final_list)
