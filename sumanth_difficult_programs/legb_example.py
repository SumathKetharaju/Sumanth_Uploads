"""
l = local
e = enclosing
g = global
b = builtin
"""
name = "mahesh"


def outer():

    global name
    name = "sasi"

    def inner():
        global name
        # nonlocal name
        name = "sumanth"
        print(name)

    inner()
    print(name)

outer()

print(name)
