input_list = [24, 56, 89, 74, 32, 16, 65, 32, 74]
second_list = [1, 2, 3, 5, 6]

new_list = input_list + second_list

print(new_list)

print(new_list * 2)

count = {}

for item in new_list:
    if item not in count:
        count[item] = 1
    else:
        count[item] += 1

print("The duplicate keys are: ")
for key, value in count.items():
    if value > 1:
        print(key, end=" ")
print()

sorted_list = []
while new_list:
    minimum = new_list[0]
    for item in new_list:
        if item < minimum:
            minimum = item
    sorted_list.append(minimum)
    new_list.remove(minimum)

print(sorted_list)

sorted_list2 = []
while input_list:
    maximum = input_list[0]

    for item in input_list:
        if item > maximum:
            maximum = item
    sorted_list2.append(maximum)
    input_list.remove(maximum)

print(sorted_list2)

new_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]
print(list(set(new_list2)))
new_list_3 = new_list2
print(new_list_3)
new_list2[0] = 10
print(new_list_3)
new_list_3[1] = 20
print(new_list2)
new_list_4 = new_list_3.copy()
print(new_list_4)
new_list_3[1] = 220
print(new_list_4)
new_list_4[1] = 120
print(new_list_3)
print(new_list_4)

for index in range(len(new_list_3)):
    print(new_list_3[index])
print()

for index in range(len(input_list)-1, -1, -1):
    print(input_list[index])

list_1 = [[1, 2], [6, 7], [8, 9]]
expected_list = []
for sub_list in list_1:
    for item in sub_list:
        expected_list.append(item)
print(expected_list)

list_comprehension = [item for sub_list in list_1 for item in sub_list]
print(list_comprehension)

for index, value in enumerate(list_1):
    print(index, value)