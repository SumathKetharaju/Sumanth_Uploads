def square_of_num(num):

    if num == int(num):
        return f"The square of given number {num} is --> {num * num}"
    else:
        return f"Your entered number {num} is in {type(num)} format, So Please Enter Valid Integer number"


print(square_of_num(2))
print(square_of_num(8))
print(square_of_num(8.2))
print("-----------------------------------------------------------------------------------------------------------")


def square_of_multiple_nums(num_1, num_2, num_3):

    if num_1 == int(num_1) and num_2 == int(num_2) and num_3 == int(num_3):
        return f"The square of given numbers {num_1}, {num_2}, {num_3} are --> {num_1 ** 2, num_2 ** 2, num_3 ** 2,}"
    elif num_1 != int(num_1):
        return f"Your entered first number {num_1} is in {type(num_1)} format, So Please Enter Valid Integer number"
    elif num_2 != int(num_2):
        return f"Your entered second number {num_2} is in {type(num_2)} format, So Please Enter Valid Integer number"
    else:
        return f"Your entered third number {num_3} is in {type(num_3)} format, So Please Enter Valid Integer number"


print(square_of_multiple_nums(2, 4, 5))
print(square_of_multiple_nums(8, 5, 1.2))
print(square_of_multiple_nums(8.2, 4, 2))
print(square_of_multiple_nums(8, 4.1, 2))
print(square_of_multiple_nums(7.3, 4.1, 2))
print("-----------------------------------------------------------------------------------------------------------")


def square_and_cube_of_num(num):

    if num == int(num):
        return f"The square and cube of given number {num} is --> {num * num, num ** 3}"
    else:
        return f"Your entered number {num} is in {type(num)} format, So Please Enter Valid Integer number"


print(square_and_cube_of_num(2))
print(square_and_cube_of_num(8))
print(square_and_cube_of_num(8.2))
print("-----------------------------------------------------------------------------------------------------------")


def addition_of_two_nums(num_1, num_2):

    if num_1 == int(num_1) and num_2 == int(num_2):
        return f"The addition of two numbers both {num_1} and {num_2} is --> {num_1 + num_2}"
    elif num_1 != int(num_1):
        return f"Your entered first number {num_1} is in {type(num_1)} format, So Please Enter Valid Integer number"
    else:
        return f"Your entered second number {num_2} is in {type(num_2)} format, So Please Enter Valid Integer number"


print(addition_of_two_nums(2, 4))
print(addition_of_two_nums(8, 4))
print(addition_of_two_nums(8, 23))
print(addition_of_two_nums(8.2, 23))
print(addition_of_two_nums(8, 23.1))
print("-----------------------------------------------------------------------------------------------------------")


def cube_and_fourth_power_of_num(num):

    if num == int(num):
        return f"The cube and cube_and_fourth_power of given number {num} is --> {num ** 3, num ** 4}"
    else:
        return f"Your entered number {num} is in {type(num)} format, So Please Enter Valid Integer number"


print(cube_and_fourth_power_of_num(2))
print(cube_and_fourth_power_of_num(8))
print(cube_and_fourth_power_of_num(5))
print(cube_and_fourth_power_of_num(8.2))
print("-----------------------------------------------------------------------------------------------------------")
