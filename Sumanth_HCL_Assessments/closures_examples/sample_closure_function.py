def outer_function():

    message = "Hi"

    def inner_function():

        print(f"This message {message} is printed from the inner function")

    return inner_function()


print("------------------------------------calling outer_function() only ------------------------------------------")
outer_function()
print()

print("-------------------------------calling outer_function() in print statement -----------------------------------")
print(f"Here we are calling outer function using 'outer_function()' in print statement "
      f"then it print as --> {outer_function()}\n")

print("-------------------------------Assigning outer_function() to new_func----------------------------------------")
new_func = outer_function()
print(f"Here we are calling outer function using 'new_func = outer_function()' in print statement "
      f"then it print as --> {new_func}\n")

# AttributeError: 'NoneType' object has no attribute '__name__'
# print(f"to print the status of function we will use --> {new_func.__name__}")
print("---------------------------------------------------------------------------------------------------------\n\n")


def outer_function_2():

    message = "Hi"

    def inner_function_2():

        print(f"This message {message} is printed from the inner function")

    return inner_function_2


print("------------------------------------calling outer_function_2() only ------------------------------------------")
outer_function_2()
print()

print("-------------------------------calling outer_function_2() in print statement -----------------------------------")
print(f"Here we are calling outer function using 'outer_function_2()' in print statement "
      f"then it print as --> \n{outer_function_2()}\n")

print("-------------------------------Assigning outer_function() to new_func_2----------------------------------------")
new_func_2 = outer_function_2()
print(f"Here we are calling outer function using 'new_func = outer_function()' in print statement "
      f"then it print as --> \n{new_func_2}\n")

print(f"Here we are calling outer function using 'new_func = outer_function()' in print statement "
      f"then it print as --> \n{new_func_2()}\n")

print(f"to print the status of function we will use --> {new_func_2.__name__}")
print("---------------------------------------------------------------------------------------------------------\n\n")
