def college():

    print("This function states the function without return statement")
    principal_name = "Sumanth"


print(f"--------------------------college()---------------------------------\n")
college()

print(f"\n----------------------------print(college())---------------------------------\n")
print(college())

print(f"\n----------------------------clg = college-------------------------------------")
print(f"\n-------------------------------print(clg)----------------------------------------\n")
clg = college
print(clg)

print(f"\n-------------------------------clg()--------------------------------------\n")
clg()

print(f"\n-----------------------------print(clg())---------------------------------------------\n")
print(clg())

print(f"\n-------------------------------clg_2 = college()---------------------------------------------\n")
print(f"\n----------------------------------print(clg_2)-------------------------------------------\n")
clg_2 = college()
print(clg_2)

print("\n----------------------------------print(clg_2())-------------------------------------------\n")
print("print(clg_2()) --> TypeError: 'NoneType' object is not callable\n")
# TypeError: 'NoneType' object is not callable
# print(clg_2())

# ---------------------------------------------------------------------------------------------------------------------
print("\n----------------------------------print(college())-------------------------------------------\n")


def college():

    print("This function states the function with return statement")
    principal_name = "Sumanth"
    return f"The college principle name is {principal_name}"


print(college())

# ---------------------------------------------------------------------------------------------------------------------
print("\n----------------------------------print(college('Sumanth'))-------------------------------------------\n")


def college(principal_name):

    print("This function states the function with single parameter")
    return f"The college principle name is {principal_name}"


print(college("Sumanth"))

# ---------------------------------------------------------------------------------------------------------------------
print("\n---------------------print(college('Sumanth', 'Royal Enfield', 'Rolls-Royce'))------------------------\n")


def college(principal_name, bike, car):

    print("This function states the function with positional parameters")
    return f"The college principle name is {principal_name} and they contain following contents {bike} and {car}"


print(college("Sumanth", "Royal Enfield", "Rolls-Royce"))

print("\n---------------------print(college('Rolls-Royce', 'Sumanth', 'Royal Enfield'))------------------------\n")

print(college("Rolls-Royce", "Sumanth", "Royal Enfield"))

# ---------------------------------------------------------------------------------------------------------------------
print("\n---------------------print(college('Sumanth', 'Bike', 'Car', 'Mobile', 'House'))------------------------\n")


def college(principal_name, *contents):

    print("This function states the function with any number of positional parameters")
    return f"The college principle name is {principal_name} and they contain following contents {contents}"


print(college("Sumanth", "Bike", "Car", "Mobile", "House"))

# ---------------------------------------------------------------------------------------------------------------------
print('\n-------------------print(college("Sumanth", bike="Royal Enfield", car="Rolls-Royce"))----------------------\n')


def college(principal_name, bike, car):

    print("This function states the function with keyword arguments")
    return f"The college principle name is {principal_name} and they contain following contents {bike, car}"


print(college("Sumanth", bike="Royal Enfield", car="Rolls-Royce"))

# ---------------------------------------------------------------------------------------------------------------------
print('\n------------------------'
'print(college("Sumanth", Bike="Royal Enfield", Car="Rolls-Royce", Mobile="Vivo", House="Srinivasulu Nilayam"))-----\n')


def college(principal_name, **contents):

    print("This function states the function with any number of keyword arguments")
    return f"The college principle name is {principal_name} and they contain following contents {contents}"


print(college("Sumanth", Bike="Royal Enfield", Car="Rolls-Royce", Mobile="Vivo", House="Srinivasulu Nilayam"))

# ---------------------------------------------------------------------------------------------------------------------
print('\n-------------------print(college())----------------------\n')


def college(principal_name="Sumanth", house="Srinivasulu Nilayam"):

    print("This function states the function with default arguments")
    return f"The college principle name is {principal_name} and his house name is {house}"


print(college())

# ---------------------------------------------------------------------------------------------------------------------

# for num in range(1, 11):
#     for n in range(1, 11):
#         print(f"{num} * {n} --> {num * n}")
#     print()
#     print(end="")
# print(end="")
