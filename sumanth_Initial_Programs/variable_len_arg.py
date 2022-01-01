def sum(a, *b):

    c = a
    for i in b:
        c = c+i
    print(c)


sum(4, 10, 12, 5, 46)