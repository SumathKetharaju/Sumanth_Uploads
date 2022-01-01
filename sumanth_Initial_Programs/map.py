nums = (3, 5, 6, 8, 9, 4, 7, 1, 2)
evens = list(filter(lambda n: n%2 ==0, nums))
doubles = list(map(lambda n:n*2, evens))
print(doubles)