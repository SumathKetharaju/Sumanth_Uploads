def college():

    print("This function states the function without return statement")
    principal_name = "Sumanth"


print("--------------------------college()---------------------------------")
print()
college()
print()
print("----------------------------print(college())---------------------------------")
print()
print(college())
print()
print("----------------------------clg = college-------------------------------------")
print()
clg = college
print()
print("-------------------------------clg()--------------------------------------")
print()
clg()
print()
# print("-------------------------------print(clg)----------------------------------------")
# print()
# print(clg)
# print()
# print("-----------------------------print(clg())---------------------------------------------")
# print()
# print(clg())
# print()
# print("-------------------------------clg = college()---------------------------------------------")
# print()
# clg = college()
# print()
# print("----------------------------------print(clg)-------------------------------------------")
# print()
# print(clg)
# print()
# print("----------------------------------print(clg())-------------------------------------------")
# print(clg())

# ---------------------------------------------------------------------------------------------------------------------

# def college():
#
#     print("This function states the function with return statement")
#     principal_name = "Sumanth"
#     return f"The college principle name is {principal_name}"
#
#
# print(college())

# ---------------------------------------------------------------------------------------------------------------------

# def college(principal_name):
#
#     print("This function states the function with single parameter")
#     return f"The college principle name is {principal_name}"
#
#
# print(college("Sumanth"))

# ---------------------------------------------------------------------------------------------------------------------

# def college(principal_name, bike, car):
#
#     print("This function states the function with parameters")
#     return f"The college principle name is {principal_name} and they contain following contents {bike} and {car}"
#
#
# print(college("Sumanth", "Royal Enfield", "Rolls-Royce"))
# print(college("Rolls-Royce", "Sumanth", "Royal Enfield"))

# ---------------------------------------------------------------------------------------------------------------------

# def college(principal_name, *contents):
#
#     print("This function states the function with any number of parameters")
#     return f"The college principle name is {principal_name} and they contain following contents {contents}"
#
#
# print(college("Sumanth", "Bike", "Car", "Mobile", "House"))

# ---------------------------------------------------------------------------------------------------------------------

# def college(principal_name, bike, car):
#
#     print("This function states the function with keyword arguments")
#     return f"The college principle name is {principal_name} and they contain following contents {bike, car}"
#
#
# print(college("Sumanth", bike="Royal Enfield", car="Rolls-Royce"))

# ---------------------------------------------------------------------------------------------------------------------
#
# def college(principal_name, **contents):
#
#     print("This function states the function with any number of keyword arguments")
#     return f"The college principle name is {principal_name} and they contain following contents {contents}"
#
#
# print(college("Sumanth", Bike="Royal Enfield", Car="Rolls-Royce", Mobile="Vivo", House="Srinivasulu Nilayam"))

# ---------------------------------------------------------------------------------------------------------------------

# def college(principal_name="Sumanth", house="Srinivasulu Nilayam"):
#
#     print("This function states the function with default arguments")
#     return f"The college principle name is {principal_name} and his house name is {house}"
#
#
# print(college())

# ---------------------------------------------------------------------------------------------------------------------

# sumanth = "I am outside the college"
# print(f"calling from outside the function(global) ---> Where are you sumanth : {sumanth}")
#
#
# def college():
#
#     print(f"calling from within current function(local) -----> Where are you sumanth : {sumanth}")
#
#
# college()
# print(f"calling from outside the function(global) before using global keyword --> Where are you sumanth : {sumanth}")

# ---------------------------------------------------------------------------------------------------------------------

# sumanth = "I am outside the college"
# print(f"calling from outside the function(global) ---> Where are you sumanth : {sumanth}")
#
#
# def college():
#
#     sumanth = "I am inside the college"
#     print(f"calling from within current function(local) -----> Where are you sumanth : {sumanth}")
#
#
# college()
# print(f"calling from outside the function(global) before using global keyword --> Where are you sumanth : {sumanth}")

# ---------------------------------------------------------------------------------------------------------------------

# sumanth = "I am outside of the college"
# print(f"calling from outside the function(global) ---> Where are you sumanth : {sumanth}")
#
#
# def college():
#
#     global sumanth
#     sumanth = "I am inside the college"
#     print(f"calling from within current function(local) -----> Where are you sumanth : {sumanth}")
#
#
# college()
# print(f"calling from outside the function(global) after using global keyword ---> Where are you sumanth : {sumanth}")

# ---------------------------------------------------------------------------------------------------------------------

# def college():
#
#     sumanth = "I am inside the college"
#     print(f"calling from within enclosing function(nonlocal) --> Where are you sumanth : {sumanth}")
#
#     def class_room():
#
#         print(f"calling from within current function(local) -----> Where are you sumanth : {sumanth}")
#
#     class_room()
#     print(f"calling from within enclosing function(nonlocal) before using nonlocal-> Where are you sumanth:{sumanth}")
#
#
# college()

# ---------------------------------------------------------------------------------------------------------------------

# def college():
#
#     sumanth = "I am inside the college"
#     print(f"calling from within enclosing function(nonlocal) --> Where are you sumanth : {sumanth}")
#
#     def class_room():
#         sumanth = "Now I am in classroom"
#         print(f"calling from within current function(local) -----> Where are you sumanth : {sumanth}")
#
#     class_room()
#     print(f"calling from within enclosing function(nonlocal) before using nonlocal -> Where are you sumanth: {sumanth}")
#
#
# college()

# ---------------------------------------------------------------------------------------------------------------------

# def college():
#
#     sumanth = "I am inside the college"
#     print(f"calling from within enclosing function(nonlocal) --> Where are you sumanth : {sumanth}")
#
#     def class_room():
#         nonlocal sumanth
#         sumanth = "Now I am in classroom"
#         print(f"calling from within current function(local) -----> Where are you sumanth : {sumanth}")
#
#     class_room()
#     print(f"calling from within enclosing function(nonlocal) after using nonlocal--> Where are you sumanth : {sumanth}")
#
#
# college()

# ---------------------------------------------------------------------------------------------------------------------

# sumanth = "I am outside of the college"
# print(f"calling from outside the function(global) ---> Where are you sumanth : {sumanth}")
#
#
# def college():
#
#     sumanth = "I am inside the college"
#     print(f"calling from within enclosing function(nonlocal) --> Where are you sumanth : {sumanth}")
#
#     def class_room():
#
#         sumanth = "Now I am in classroom"
#         print(f"calling from within current function(local) -----> Where are you sumanth : {sumanth}")
#
#     class_room()
#     print(f"calling from within enclosing function(nonlocal) before using nonlocal--> Where are you sumanth : {sumanth}")
#
#
# college()
# print(f"calling from outside the function(global) before using global keyword ---> Where are you sumanth : {sumanth}")

# ---------------------------------------------------------------------------------------------------------------------

# sumanth = "I am outside of the college"
# print(f"calling from outside the function(global) ---> Where are you sumanth : {sumanth}")
#
#
# def college():
#
#     sumanth = "I am inside the college"
#     print(f"calling from within enclosing function(nonlocal) --> Where are you sumanth : {sumanth}")
#
#     def class_room():
#         nonlocal sumanth
#         sumanth = "Now I am in classroom"
#         print(f"calling from within current function(local) -----> Where are you sumanth : {sumanth}")
#
#     class_room()
#     print(f"calling from within enclosing function(nonlocal) after using nonlocal--> Where are you sumanth : {sumanth}")
#
#
# college()
# print(f"calling from outside the function(global) after using nonlocal ---> Where are you sumanth : {sumanth}")

# ---------------------------------------------------------------------------------------------------------------------

# sumanth = "I am outside of the college"
# print(f"calling from outside the function(global) ---> Where are you sumanth : {sumanth}")
#
#
# def college():
#
#     sumanth = "I am inside the college"
#     print(f"calling from within enclosing function(nonlocal) --> Where are you sumanth : {sumanth}")
#
#     def class_room():
#
#         global sumanth
#         sumanth = "Now I am in classroom"
#         print(f"calling from within current function(local) -----> Where are you sumanth : {sumanth}")
#
#     class_room()
#     print(f"calling from within enclosing function(nonlocal) after using global--> Where are you sumanth : {sumanth}")
#
#
# college()
# print(f"calling from outside the function(global) after using global keyword ---> Where are you sumanth : {sumanth}")

# ---------------------------------------------------------------------------------------------------------------------

# sumanth = "I am outside of the college"
# print(f"calling from outside the function(global) ---> Where are you sumanth : {sumanth}")
#
#
# def college():
#
#     global sumanth
#     sumanth = "I am inside the college"
#     print(f"calling from within enclosing function(nonlocal) --> Where are you sumanth : {sumanth}")
#
#     def class_room():
#         global sumanth
#         sumanth = "Now I am in classroom"
#         print(f"calling from within current function(local) -----> Where are you sumanth : {sumanth}")
#
#     class_room()
#     print(f"calling from within enclosing function(nonlocal) after using global--> Where are you sumanth : {sumanth}")
#
#
# college()
# print(f"calling from outside the function(global) after using global keyword ---> Where are you sumanth : {sumanth}")

# ---------------------------------------------------------------------------------------------------------------------

addition = lambda x, y: x+y
print(f"The sum of two numbers is {addition(20, 30)}")

subtraction = lambda x, y: x-y
print(f"The subtraction of two numbers is {subtraction(50, 30)}")
#
multiplication = lambda x, y: x*y
print(f"The multiplication of two numbers is {multiplication(5, 3)}")

division = lambda x, y: x/y
print(f"The division of two numbers is {division(15, 3)}")

remainder = lambda x: x % 2
print(f"The remainder of number is {remainder(15)}")

# --------------------------------------------------------------------------------------------------------------------

input_list = [12, 56, 89, 47, 23, 32, 24]

addition_of_list_of_nums_with_10 = map(lambda x: x + 10, input_list)
print(f"The list of addition of numbers with 10 are : {list(addition_of_list_of_nums_with_10)}")

subtraction_of_list_of_nums_with_10 = map(lambda x: x - 10, input_list)
print(f"The list of subtraction of numbers with 10 are : {list(subtraction_of_list_of_nums_with_10)}")

multiplication_of_list_of_nums_with_2 = map(lambda x: x * 2, input_list)
print(f"The list of multiplication of numbers with 2 are : {list(multiplication_of_list_of_nums_with_2)}")

division_of_list_of_nums_with_2 = map(lambda x: x / 2, input_list)
print(f"The list of divisions of numbers with 2 are : {list(division_of_list_of_nums_with_2)}")

remainders_of_list_of_nums_with_2 = map(lambda x: x % 2 == 0, input_list)
print(f"The list of remainders are : {list(remainders_of_list_of_nums_with_2)}")

# --------------------------------------------------------------------------------------------------------------------

sample_list = [12, 56, 89, 47, 23, 32, 24, 84]
even_nums = filter(lambda x: x % 2 == 0, sample_list)
print(f"The list of even numbers are : {list(even_nums)}")

odd_nums = filter(lambda x: x % 2 != 0, sample_list)
print(f"The list of odd numbers are : {list(odd_nums)}")

sample_list_2 = [12, 56, 89, 47, "Sumanth", 23, 32, "HCL", 24, 84]
strings = filter(lambda x: type(x) == str, sample_list_2)
print(f"The list of strings are : {list(strings)}")

integers = filter(lambda x: type(x) == int, sample_list_2)
print(f"The list of integers are : {list(integers)}")

# --------------------------------------------------------------------------------------------------------------------

# two_power_nums = [2 ** x for x in range(1, 10)]
# print(f"The list of two power nums are : {two_power_nums}")
#
# square_of_nums = [x ** 2 for x in range(1, 10)]
# print(f"The list of square of nums are {square_of_nums}")

