list_comp = [x for x in range(1, 10) if x % 2 == 0]
print(list_comp)

list_comp_2 = [x if x % 2 == 0 else x**2 for x in range(1, 10)]
print(list_comp_2)

sample = lambda x: x + x
print(sample(2))

sample_2 = lambda x, y: x + y
print(sample_2(2, 5))

sample_3 = map(lambda x: x ** 2, list_comp)
print(sample_3)
print(list(sample_3))

sample_4 = filter(lambda x: x % 2 == 0, range(1, 20))
print(sample_4)
print(list(sample_4))
