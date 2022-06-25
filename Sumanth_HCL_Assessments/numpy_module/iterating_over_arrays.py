import numpy

sample_array = numpy.arange(10)**3
print(f"Given Created Sample array when we given 'sample_array = numpy.arange(10)**3' is --> {sample_array}")

print(f"To Print the Elements in one by one are ---> ")
for num in sample_array:
    print(num)

print(f"Above Elements Printed as one by one\n")

companies = numpy.array([["Samsung", "Microsoft", "IBM", "Spotify", "Flipkart"],
                         [1938, 1975, 1911, 2006, 2007],
                         [489000, 131000, 380000, 3000, 30000]])

i = 0
for row in companies:
    print(f"Row number {i} contains --> {row}")
    i += 1

print("Iteration is Completed\n")

companies.flatten()
print(f"Companies after using flatten function like 'companies.flatten()' is --> \n{companies}\n")

print(f"To Print the companies data in one by one like 'companies.flatten(order="F")' are ---> ")
for data in companies.flatten(order="F"):
    print(data)

print(f"Companies data Printed as one by one\n")

nums_array = numpy.arange(16).reshape(4, 4)
print(f"Given Created nums array when we given 'nums_array = numpy.arange(16).reshape(4, 4)' is --> \n{nums_array}\n")

print(f"To Print the nums_array Elements in 'numpy.nditer(nums_array)'  one by one are ---> ")
for num in numpy.nditer(nums_array):
    print(num)
print(f"nums_array Printed as one by one\n")

print(f"To Print the nums_array Elements when we use Order in 'numpy.nditer(nums_array, order="F")' one by one are ---> ")
for num in numpy.nditer(nums_array, order="F"):
    print(num)
print(f"nums_array Printed when we use Order as one by one\n")

print(f"To Print the nums_array Elements when we use Order and flags in 'numpy.nditer(nums_array, order="F")' one by one are ---> ")
for num in numpy.nditer(nums_array, order="F", flags=["external_loop"]):
    print(num)
print(f"nums_array Printed when we use Order and flags as one by one\n")

# print(f"To apply operation on each nums_array Elements when we give 'array[...] = array * array' one by one are ---> ")
# ValueError: assignment destination is read-only


# for array in numpy.nditer(nums_array):
#     array[...] = array * array
# print(f"nums_array Printed when we use Order and flags as one by one\n")

print(f"To apply operation on each nums_array Elements when have to give op_flags like 'op_flags=["'readwrite'"]' one by one are ---> ")
for array in numpy.nditer(nums_array, op_flags=["readwrite"]):
    array[...] = array * array
print(f"nums_array Printed when we use op_flags = \n{nums_array}\n")
