def person(name, age, behaviour):

    print(f"My name is {name}")
    print(f"{name} age is {age}")
    print(f"{name} behaviour is {behaviour}")
    return f"his full name is {name}"
    # return "My name is {name}" - it give error because function access only one return statement


person("sujith", 26, "good")
print()


mahesh = person("mahesh", 24, "good")
print(mahesh)
print()

my_name = "sasi"
my_age = 23
my_behaviour = "good"
person(my_name, my_age, my_behaviour)
print()

print(person("sumanth", 25, "not bad"))
print()
