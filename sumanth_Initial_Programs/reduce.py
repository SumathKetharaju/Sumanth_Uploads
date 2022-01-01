from functools import reduce
# def add_all(a, b):

 # return a+b


nums = (3, 5, 6, 8, 9, 4, 7, 1, 4)
evens = list(filter(lambda n: n%2 ==0, nums))
doubles = list(map(lambda n:n*2, evens))
# sum = reduce(add_all, doubles)
sum = reduce(lambda a, b: a+b,doubles)
print(sum)
