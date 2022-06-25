""" -------------------------------------This is an example for decorator-------------------------------------------"""

# decorator function


def make_up_man(another_function):

    # Wrapper function
    def make_up_kit():
        print(f"{another_function.__name__} is sitted in chair")
        print(f"make_up_man applies some creams to {another_function.__name__}")
        return another_function()
    return make_up_kit

@make_up_man
def person_1():
    print("Now he is going to wedding")

@make_up_man
def person_2():
    print(f"Now he is also ready to go to marriage with gift")


person_1()
person_2()

