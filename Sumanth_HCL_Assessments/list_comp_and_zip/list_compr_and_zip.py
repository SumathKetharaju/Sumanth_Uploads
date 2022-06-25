two_power_nums = [2 ** x for x in range(1, 10)]
print(f"The list of two power nums upto 10 are :--> {two_power_nums}\n")

square_of_nums = [x ** 2 for x in range(1, 10)]
print(f"The list of square of nums upto 10 are --> {square_of_nums}\n")

even_nums = [x for x in range(1, 20) if x % 2 == 0]
print(f"The list of even nums are --> {even_nums}\n")

odd_nums = [x for x in range(1, 20) if x % 2 != 0]
print(f"The list of odd nums are --> {odd_nums}\n")

odd_nums_and_remainders_with_2 = [x if x % 2 != 0 else x % 2 for x in range(1, 20)]
print(f"The list of odd_nums_and_remainders_with_2 are --> {odd_nums_and_remainders_with_2}\n")

even_nums_and_remainders_with_2 = [x if x % 2 == 0 else x % 2 for x in range(1, 20)]
print(f"The list of even_nums_and_remainders_with_2 are --> {even_nums_and_remainders_with_2}\n")
print("----------------------------------------------------------------------------------------------------------")

list_1 = [12, 36, 96, 32, 58, 46, 94]
list_2 = [15, 63, 85, 49, 76, 25, 37]
print(f"Given List one is --> {list_1}")
print(f"Given List two is --> {list_2}\n")
combination_of_lists = zip(list_1, list_2)

# output--> <zip object at 0x000001AABC544940>
print(f"The address of zip function object when we assign 'combination_of_lists = zip(list_1, list_2)' "
      f"is --> {combination_of_lists}\n")

# output--> [(12, 15), (36, 63), (96, 85), (32, 49), (58, 76), (46, 25), (94, 37)]
# print(f"To print combination_of_lists in a single list using "
#       f"'list(combination_of_lists)' is --> {list(combination_of_lists)}\n")

# output --> {12: 15, 36: 63, 96: 85, 32: 49, 58: 76, 46: 25, 94: 37}
# print(f"To print combination_of_lists in a single dict using "
#       f"'dict(combination_of_lists)' is --> {dict(combination_of_lists)}\n")

# ouput --> ((12, 15), (36, 63), (96, 85), (32, 49), (58, 76), (46, 25), (94, 37))
# print(f"To print combination_of_lists in a single tuple using "
#       f"'tuple(combination_of_lists)' is --> {tuple(combination_of_lists)}\n")

# ouyput --> {(96, 85), (32, 49), (46, 25), (12, 15), (94, 37), (36, 63), (58, 76)}
print(f"To print combination_of_lists in a single set using "
      f"'set(combination_of_lists)' is --> {set(combination_of_lists)}\n")
print("----------------------------------------------------------------------------------------------------------\n")
# --------------------------------------------------------------------------------------------------------------------

list_3 = [12, 36, [96, 32], 58, 94]
list_4 = [15, [63, 85], 49, 76, 25, 37]

combination_of_nested_lists = zip(list_3, list_4)

print(f"The address of zip function object when we assign 'combination_of_nested_lists = zip(list_3, list_4)' "
      f"is --> {combination_of_nested_lists}\n")

# output--> [(12, 15), (36, [63, 85]), ([96, 32], 49), (58, 76), (94, 25)]
# print(f"To print combination_of_nested_lists in a single list using "
#       f"'list(combination_of_nested_lists)' is --> {list(combination_of_nested_lists)}\n")

# output --> ((12, 15), (36, [63, 85]), ([96, 32], 49), (58, 76), (94, 25))
# print(f"To print combination_of_nested_lists in a single tuple using "
#       f"'tuple(combination_of_nested_lists)' is --> {tuple(combination_of_nested_lists)}\n")

# output --> TypeError: unhashable type: 'list'
# print(f"To print combination_of_nested_lists in a single set using "
#       f"'set(combination_of_nested_lists)' is --> {set(combination_of_nested_lists)}\n")

# output --> TypeError: unhashable type: 'list'
# print(f"To print combination_of_nested_lists in a single dict using "
#       f"'dict(combination_of_nested_lists)' is --> {dict(combination_of_nested_lists)}\n")

# --------------------------------------------------------------------------------------------------------------------

tuple_1 = (12, 36, 96, 32, 58, 94)
tuple_2 = (15, 63, 85, 49, 76, 25, 37)

combination_of_tuples = zip(tuple_1, tuple_2)
# print(combination_of_tuples)  # output-->  <zip object at 0x0000024E406E4C00>
# print(list(combination_of_tuples))  # output--> [(12, 15), (36, 63), (96, 85), (32, 49), (58, 76), (94, 25)]
# print(tuple(combination_of_tuples))  # output--> ((12, 15), (36, 63), (96, 85), (32, 49), (58, 76), (94, 25))
# print(set(combination_of_tuples))  # output--> {(96, 85), (32, 49), (94, 25), (12, 15), (36, 63), (58, 76)}
# print(dict(combination_of_tuples))  # output--> {12: 15, 36: 63, 96: 85, 32: 49, 58: 76, 94: 25}

# --------------------------------------------------------------------------------------------------------------------
