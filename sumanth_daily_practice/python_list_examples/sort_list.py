input_list = [14, 52, 5, 8, 65, 45, 92, 58, 32, 16, 1]

input_list.sort()

print(input_list)

sorted_list = []

while input_list:
    minimum = input_list[0]
    for item in input_list:
        if item < minimum:
            minimum = item
    sorted_list.append(minimum)
    input_list.remove(minimum)

print(sorted_list)

input_list_2 = [14, 52, 5, 8, 65, 45, 92, 58, 32, 16, 1]

max_element = []

while input_list_2:
    maximum = input_list_2[0]
    for item in input_list_2:
        if item > maximum:
            maximum = item
    max_element.append(maximum)
    input_list_2.remove(maximum)

print(max_element)

for i in range(len(input_list_2)):
    for j in range(1, len(input_list_2)):
        if input_list_2[j-1] > input_list_2[j]:
            input_list_2[j-1], input_list_2[j] = input_list_2[j], input_list_2[j-1]

print(input_list_2)
