def update(x):
    print(id(x))
    x = 8
    print(id(x))

    print('x', x)


a = 15
print(id(a))
update(15)
print('a', a)