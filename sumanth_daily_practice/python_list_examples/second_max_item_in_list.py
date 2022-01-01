input_list = [54, 12, 63, 548, 965, 235]

max_element = []

while input_list:
    maximum = input_list[0]
    for item in input_list:
        if item > maximum:
            maximum = item
    max_element.append(maximum)
    input_list.remove(maximum)

print(max_element)
