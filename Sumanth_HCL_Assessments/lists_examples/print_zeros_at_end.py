sample_list = [8, 0, 0, 65, 79, 0, 21, 0, 0, 0, 54, 12]
#
zero = 0
#
for num in sample_list:
    print(f"sample_list -> {sample_list} and here the num is {num} and its index is {sample_list.index(num)}")
    if num == zero:
        # print(sample_list)
        sample_list.append(num)
        print(f"sample_list after appending -> {sample_list} and its num {num} its index is {sample_list.index(num)}")
        sample_list.remove(num)
        print(f"sample_list after removing --------------> {sample_list} and its num {num} its index is {sample_list.index(num)}")
#
print(f"sample list after changing zeros from current position to end of the list using remove method --> {sample_list}\n")


for index in range(len(sample_list)):
    print(f"sample_list -> {sample_list} and its num {sample_list[index]} and its index is {index}")
    if sample_list[index] == zero:
        # print(sample_list)
        sample_list.append(sample_list[index])
        print(f"sample_list after appending -> {sample_list} and its num {sample_list[index]} its index is {index}")
        sample_list.pop(index)
        print(f"sample_list after removing --------------> {sample_list} and its num {sample_list[index]} its index is {index}")

print(f"sample list after changing zeros from current position to end of the list using pop method --> {sample_list}")

