import random

# There are 3 numeric types in python
# int,float,complex

# Type conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that
# can be used to make random numbers:

print(random.randrange(1, 10))