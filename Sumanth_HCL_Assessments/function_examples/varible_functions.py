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