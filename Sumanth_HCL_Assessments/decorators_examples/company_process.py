def make_up_man(another_function):

    def make_up_kit(*args, **kwargs):
        print(f"{another_function.__name__} is sitted in chair")
        print(f"make_up_man applies some creams to {another_function.__name__}")
        return another_function(*args, **kwargs)
    return make_up_kit

@make_up_man
def person_1():
    print("Now he is ready to go to marriage")

@make_up_man
def person_2(gift):
    print(f"Now he is also ready to go to marriage with {gift}")

person_1()
person_2("Watch")