a = 10
print(id(a))
def somethimg():

    a = 15
    x = globals() ['a']
    print(id(x))
    print("in fun", a)
    globals()['a'] = 9



somethimg()
print("out side", a)
