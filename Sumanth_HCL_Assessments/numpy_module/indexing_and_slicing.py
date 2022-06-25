import numpy

input_array = numpy.arange(10) ** 3

print(f"The Generated input array when we use 'input_array = numpy.arange(10) ** 3' is --> {input_array}\n")
print(f"Third index of the array using positive index i.e 'input_array[3]' is --> {input_array[3]}\n")
print(f"Third index of the array from last using negative index is 'input_array[-4]' is --> {input_array[-4]}\n")
print(f"Slicing of the array from first to eight index using positive slicing is 'input_array[1:8]' is --> {input_array[1:8]}\n")
print(f"Slicing from Third to -Third index using both positive and negative slicing is 'input_array[3:-3]' is --> {input_array[3:-3]}\n")
print(f"Slicing from starting to eight index using both positive slicing is 'input_array[:8]' is --> {input_array[:8]}\n")
print(f"Slicing from third to end index using both positive slicing is 'input_array[3:]' is --> {input_array[3:]}\n")
print(f"Slicing from starting to tenth index with step size 2 using both positive slicing is 'input_array[:10:2]' is --> {input_array[:10:2]}\n")
print(f"Slicing when we use only step[ size -1 negative slicing is 'input_array[::-1]' is --> {input_array[::-1]}\n")

companies = numpy.array([["Samsung", "Microsoft", "IBM", "Spotify", "Flipkart"],
                         [1938, 1975, 1911, 2006, 2007],
                         [489000, 131000, 380000, 3000, 30000]], dtype="<U9")

print(f"The Created companies are --> \n{companies}\n")
print(f"The Zeroth index of Created companies 'companies[0]' are --> \n{companies[0]}\n")
print(f"The Second index of Created companies 'companies[2]' are --> \n{companies[2]}\n")
print(f"The First index of Created companies 'companies[1]' are --> \n{companies[1]}\n")
print(f"The Third column of Created companies 'companies[:,2]' are --> \n{companies[:,2]}\n")
print(f"The Fifth column of Created companies 'companies[:,4]' are --> \n{companies[:,4]}\n")
print(f"The Second element of zeroth index of the Created companies 'companies[0, 2]' are --> \n{companies[0,2]}\n")
print(f"The Third element of second index of the Created companies 'companies[2, 3]' are --> \n{companies[2, 3]}\n")

print(f"The Third element of second index of the Created companies 'companies[0:2, 2:4]' are --> \n{companies[0:2, 2:4]}\n")
print(f"The Third element of second index of the Created companies 'companies[:, 2:4]' are --> \n{companies[:, 2:4]}\n")
print(f"The Third element of second index of the Created companies 'companies[:, 2:4]' are --> \n{companies[-1, :]}\n")
print(f"The Third element of second index of the Created companies 'companies[:, 2:4]' are --> \n{companies[0, ...]}\n")
print(f"The Third element of second index of the Created companies 'companies[:, 2:4]' are --> \n{companies[..., 2]}\n")
