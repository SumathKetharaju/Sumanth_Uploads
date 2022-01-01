def sample(input_list):

    for item in input_list:
        yield item


list = [87, 96, 54, 21]

iterator = sample(list)

print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
