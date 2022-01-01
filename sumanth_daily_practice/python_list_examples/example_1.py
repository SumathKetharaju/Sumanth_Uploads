input_list = [24, 58, 96, 32, 57, 82]
print(f"Given input is {input_list}\n")

input_list[6:] = input_list[0], input_list[1]
print(input_list)
input_list.pop(0)
print(input_list)
input_list[0] = input_list[-3]
print(input_list, "\n")
input_list.pop(-3)
print(f"final output is {input_list}")

# for index in range(len(input_list)):
#     if index == index and index + 1 == index + 1:
#         print(input_list)
#         input_list[:index] = input_list[-1]
#         print(input_list)
#         input_list[-1:] = ([input_list[index], input_list[index+1]])
#         print(input_list)
#         # input_list[-2] = input_list[index+1]
#         # input_list.remove(input_list[index])
#         input_list.remove(input_list[index])
#         print(input_list)
#         input_list.remove(input_list[index+1])
#         print(input_list)
#         print(input_list)
#         break

