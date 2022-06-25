"""
set -->
set is an unordered collection of unique elements
set cannot contain mutable elements like lists, dictionaries it can contain only immutable tuples
set does not allow duplicates, I mean if we try to add duplicates to sets it will add the element exactly once
set elements cannot be looked up by index
set can perform set operations like union, intersection, difference

comparision between lists and sets -->
lists are ordered collection but set is an unordered collection
lists can contain duplicates but set cannot contain duplicates
"""

input_set = {153, 12, 83, 5, 1982, "a", "s", "A", "Z", "sasi", "Sumanth", "Mahesh", "mani"}

print("----------------------------------Initial set---------------------------------------------------------")
print(f"Initial input set is --> {input_set}")
print(f"length of initial input set is --> {len(input_set)}")

input_set.add(3)   # set default convert elements in ascending or decending order
input_set.update([53, 47])
input_set.update({35, 74})
input_set.update((58, 49))
input_set.update("Jafrulla")
input_set.update(["Rakesh", "praveen"])
input_set.update("Jafrulla")
input_set.add(4)

# print("-"*170)
print("----------------------------------addition---------------------------------------------------------")
print(f"Middle input set is --> {input_set}")
print(f"length of Middle input set is --> {len(input_set)}")

print("-----------------------------------deletion--------------------------------------------------------")
print(f"Middle input set is --> {input_set}")
input_set.pop()
print(f"Middle input set is --> {input_set}")
print(f"length of Middle set is --> {len(input_set)}")
print(f"Popped item of input_set.pop() --> {input_set.pop()}")
print(f"Middle input set is --> {input_set}")
print(f"length of Middle input set is --> {len(input_set)}")

input_set.remove("praveen")
input_set.discard("sasi")
# print(f"removed item of input_set.remove() --> {input_set.remove('praveen')}")  # KeyError: 'praveen'

print("-------------------------------final result------------------------------------------------------------")
print(f"Final set is --> {input_set}")
print(f"length of final input set is --> {len(input_set)}")
print("-------------------------------------------------------------------------------------------")

sample_set = {153, 12, 83, 5, 1982, "a", "s", "A", "Z", "sasi", "Sumanth", "Mahesh", "mani"}

print("--------------------------------sample set---------------------------------------------")
print(f"Initial sample set is --> {sample_set}")
print(f"length of initial sample set is --> {len(sample_set)}")

print("-----------------------------------set union--------------------------------------------------------")

union_set = input_set | sample_set
print(f"Initial sample set is --> {sample_set}")
print(f"final input set is --> {input_set}")
print(f"union elements of both input set and sample set is {union_set}")
print(f"length of union set is --> {len(union_set)}")

print("-----------------------------------set intersection--------------------------------------------------------")

common_elements_of_set = input_set & sample_set
print(f"Initial sample set is --> {sample_set}")
print(f"final input set is --> {input_set}")
print(f"common elements of both input set and sample set is {common_elements_of_set}")
print(f"length of common set is --> {len(common_elements_of_set)}")

print("-----------------------------------set difference--------------------------------------------------------")

difference_elements_of_set = input_set - sample_set
print(f"Initial sample set is --> {sample_set}")
print(f"final input set is --> {input_set}")
print(f"difference of both input set and sample set is {difference_elements_of_set}")
print(f"length of difference set is --> {len(difference_elements_of_set)}")

print("-----------------------------------set symmetric difference---------------------------------------------------")

symmetric_difference_elements_of_set = input_set ^ sample_set
print(f"Initial sample set is --> {sample_set}")
print(f"final input set is --> {input_set}")
print(f"symmetric difference of both input set and sample set is {symmetric_difference_elements_of_set}")
print(f"length of symmetric difference set is --> {len(symmetric_difference_elements_of_set)}")


# for item in input_set:
#     # print(item)
#     if item is int(item):
#         # print(f"ascii value of {item} is --> {chr(item)}")
#         print("Hi")
#     elif item is str(item):
#         # print(f"ascii value of {item} is --> {chr(item)}")
#         print("Bi")
#
#     else:
#         pass






# print(set.__dict__)
# print(list.__dict__)
# print(list.__dict__)
