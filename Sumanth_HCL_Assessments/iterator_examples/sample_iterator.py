input_list = [12, 36, 54, 86, 42]

# TypeError: 'list' object is not an iterator
# print(next(input_list))

print(f"Printing each number from the input list using for loop -->")
for num in input_list:
    print(num)
print()

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
# 'reverse', 'sort']
print(f"Calling all methods available in input_list using dir(input_list) --> \n{dir(input_list)}\n")
print()

iterable = iter(input_list)
print("Printing each number from the input list using next(iterable) here iterable = iter(input_list) -->")
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
print()
# StopIteration
# print(next(iterable))

iterable_2 = input_list.__iter__()
print("Printing each number from the input list using next(iterable) here iterable_2 = input_list.__iter__() -->")
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
print(next(iterable_2))
# StopIteration
# print(next(iterable_2))


