def count(lst):

    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [2, 6, 9, 5, 8, 4, 11, 53, 89]
even, odd = count(lst)
print("even : {}, odd : {} ".format(even, odd))