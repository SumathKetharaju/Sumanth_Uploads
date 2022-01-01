# This program will use mutiplie returns for multiple functions like add, subtract, multiply and division

input_function = input("Enter the operation?")

input_raw_values = input("Enter the values?")

input_values = input_raw_values.split(" ")
# "2 3"
# "2","3"



def add(a, b):
    sum_value = a+b
    # print(sum_value)
    return sum_value


def subtract(a, b):
    subtract_value=a-b
    # print(subtract_value)
    return subtract_value


def multiply(a, b):
    multiply_value = a*b
    # print(multiply_value)
    return multiply_value


def division(a, b):
    division_value = a / b
    # print(division_value)
    return division_value

if input_function != "finish":
    if input_function == "add":
        return_value = add(int(input_values[0]), int(input_values[1]))
    if input_function == "subtract":
        return_value = subtract(int(input_values[0]), int(input_values[1]))
    if input_function == "multiply":
        return_value = multiply(int(input_values[0]), int(input_values[1]))
    if input_function == "division":
        return_value = division(int(input_values[0]), int(input_values[1]))
    print("The given function is {} and the result is {}".format(input_function, return_value))










