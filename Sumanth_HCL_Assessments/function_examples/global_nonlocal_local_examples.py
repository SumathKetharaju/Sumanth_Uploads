print("\n----------------------------------function with global variable only --------------------------------------\n")
sumanth = "I am outside of the college"
print(f"calling sumanth before creating the function ---> Where are you sumanth : {sumanth}")


def college():

    print(f"calling sumanth from within current function(local) -----> Where are you sumanth : {sumanth}")


college()
print(f"calling sumanth from outside of the function(global) after creating the function "
      f"before using global keyword --> Where are you sumanth : {sumanth}\n")

# ---------------------------------------------------------------------------------------------------------------------

print("------------------------------------function with global and local variables ------------------------------\n")
sumanth = "I am outside of the college"
print(f"calling sumanth before creating the function ---> Where are you sumanth : {sumanth}")


def college():

    sumanth = "I am inside the college"
    print(f"calling sumanth from within current function(local) -----> Where are you sumanth : {sumanth}")


college()
print(f"calling sumanth from outside of the function(global) after creating the function "
      f"before using global keyword --> Where are you sumanth : {sumanth}\n")

# ---------------------------------------------------------------------------------------------------------------------

print("--------------------function with global and local variables, global keyword ------------------------------\n")
sumanth = "I am outside of the college"
print(f"calling sumanth before creating the function ---> Where are you sumanth : {sumanth}")


def college():

    global sumanth
    sumanth = "I am inside the college"
    print(f"calling sumanth from within current function(local) -----> Where are you sumanth : {sumanth}")


college()
print(f"calling sumanth from outside of the function(global) after creating the function "
      f"after using global keyword ---> Where are you sumanth : {sumanth}\n")

# ---------------------------------------------------------------------------------------------------------------------

print("--------------------------------- Nested function with nonlocal variable ------------------------------------\n")


def college():

    sumanth = "I am inside the college"
    print(f"calling sumanth from within enclosing function(nonlocal) "
          f"before creating the nested function --> Where are you sumanth : {sumanth}")

    def class_room():

        print(f"calling sumanth from within current function(local) -----> Where are you sumanth : {sumanth}")

    class_room()
    print(f"calling sumanth from within enclosing function(nonlocal) after creating the nested function, "
          f"before using nonlocal-> Where are you sumanth:{sumanth}\n")


college()

# ---------------------------------------------------------------------------------------------------------------------

print("----------------------- Nested function with local and nonlocal variables -------------------------------\n")


def college():

    sumanth = "I am inside the college"
    print(f"calling sumanth from within enclosing function(nonlocal) "
          f"before creating the nested function --> Where are you sumanth : {sumanth}")

    def class_room():
        sumanth = "Now I am in classroom"
        print(f"calling sumanth from within current function(local) -----> Where are you sumanth : {sumanth}")

    class_room()
    print(f"calling sumanth from within enclosing function(nonlocal) after creating the nested function, "
          f"before using nonlocal -> Where are you sumanth: {sumanth}\n")


college()

# ---------------------------------------------------------------------------------------------------------------------

print("------------------ Nested function with local and nonlocal variables, nonlocal keyword ---------------------\n")


def college():

    sumanth = "I am inside the college"
    print(f"calling sumanth from within enclosing function(nonlocal) "
          f"before creating the nested function --> Where are you sumanth : {sumanth}")

    def class_room():
        nonlocal sumanth
        sumanth = "Now I am in classroom"
        print(f"calling sumanth from within current function(local) -----> Where are you sumanth : {sumanth}")

    class_room()
    print(f"calling sumanth from within enclosing function(nonlocal) after creating the nested function,"
          f" after using nonlocal--> Where are you sumanth : {sumanth}\n")


college()

# ---------------------------------------------------------------------------------------------------------------------

print("---------------------- Nested function with global, local and nonlocal variables --------------------------\n")


sumanth = "I am outside of the college"
print(f"calling sumanth before creating the function ---> Where are you sumanth : {sumanth}")


def college():

    sumanth = "I am inside the college"
    print(f"calling sumanth from within enclosing function(nonlocal) "
          f"before creating the nested function --> Where are you sumanth : {sumanth}")

    def class_room():

        sumanth = "Now I am in classroom"
        print(f"calling sumanth from within current function(local) -----> Where are you sumanth : {sumanth}")

    class_room()
    print(f"calling sumanth from within enclosing function(nonlocal) after creating the nested function,"
          f" before using nonlocal--> Where are you sumanth : {sumanth}")


college()
print(f"calling sumanth from outside the function(global) afetr  creating the function "
      f"before using global keyword ---> Where are you sumanth : {sumanth}\n")

# ---------------------------------------------------------------------------------------------------------------------

print("---------------- Nested function with global, local and nonlocal variables, non local keyword  -------------\n")


sumanth = "I am outside of the college"
print(f"calling sumanth before creating the function ---> Where are you sumanth : {sumanth}")


def college():

    sumanth = "I am inside the college"
    print(f"calling sumanth from within enclosing function(nonlocal) "
          f"before creating the nested function--> Where are you sumanth : {sumanth}")

    def class_room():
        nonlocal sumanth
        sumanth = "Now I am in classroom"
        print(f"calling sumanth from within current function(local) -----> Where are you sumanth : {sumanth}")

    class_room()
    print(f"calling sumanth from within enclosing function(nonlocal) after creating the nested function,"
          f"after using nonlocal--> Where are you sumanth : {sumanth}")


college()
print(f"calling sumanth from outside of the function(global) after creating the function,"
      f"before using global ---> Where are you sumanth : {sumanth}\n")

# ---------------------------------------------------------------------------------------------------------------------

print("---------------- Nested function with global, local and nonlocal variables, global keyword  -------------\n")
sumanth = "I am outside of the college"
print(f"calling sumanth before creating the function ---> Where are you sumanth : {sumanth}")


def college():

    sumanth = "I am inside the college"
    print(f"calling sumanth from within enclosing function(nonlocal) "
          f"before creating the nested function --> Where are you sumanth : {sumanth}")

    def class_room():

        global sumanth
        sumanth = "Now I am in classroom"
        print(f"calling sumanth from within current function(local) -----> Where are you sumanth : {sumanth}")

    class_room()
    print(f"calling sumanth from within enclosing function(nonlocal) after creating the nested function,"
          f" after using global --> Where are you sumanth : {sumanth}")


college()
print(f"calling sumanth from outside the function(global) after creating the function,"
      f"after using global keyword ---> Where are you sumanth : {sumanth}\n")

# ---------------------------------------------------------------------------------------------------------------------

print("---------------- Nested function with global, local and nonlocal variables, two global keywords  ------------\n")
sumanth = "I am outside of the college"
print(f"calling sumanth before creating the function ---> Where are you sumanth : {sumanth}")


def college():

    global sumanth
    sumanth = "I am inside the college"
    print(f"calling sumanth from within enclosing function(nonlocal) "
          f"before creating the nested function--> Where are you sumanth : {sumanth}")

    def class_room():
        global sumanth
        sumanth = "Now I am in classroom"
        print(f"calling sumanth from within current function(local) -----> Where are you sumanth : {sumanth}")

    class_room()
    print(f"calling sumanth from within enclosing function(nonlocal) after creating the nested function"
          f"after using global--> Where are you sumanth : {sumanth}")


college()
print(f"calling sumanth from outside the function(global) after creating the function "
      f"after using global keyword ---> Where are you sumanth : {sumanth}")

# ---------------------------------------------------------------------------------------------------------------------

