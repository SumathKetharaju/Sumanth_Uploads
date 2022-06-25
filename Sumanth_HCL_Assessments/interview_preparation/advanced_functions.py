list_1 = [12, 36, 96, 32, 58, 46, 94]
list_2 = [15, 63, 85, 49, 76, 25, 37]

combination_of_lists = zip(list_1, list_2)
# print(combination_of_lists)  # output--> <zip object at 0x000001AABC544940>
# print(list(combination_of_lists))  # output--> [(12, 15), (36, 63), (96, 85), (32, 49), (58, 76), (46, 25), (94, 37)]
# print(dict(combination_of_lists))   # output--> {12: 15, 36: 63, 96: 85, 32: 49, 58: 76, 46: 25, 94: 37}
# print(tuple(combination_of_lists)) # output-->  ((12, 15), (36, 63), (96, 85), (32, 49), (58, 76), (46, 25), (94, 37))
# print(set(combination_of_lists))   # output-->  {(96, 85), (32, 49), (46, 25), (12, 15), (94, 37), (36, 63), (58, 76)}

# --------------------------------------------------------------------------------------------------------------------

list_1 = [12, 36, [96, 32], 58, 94]
list_2 = [15, [63, 85], 49, 76, 25, 37]

combination_of_nested_lists = zip(list_1, list_2)
# print(combination_of_nested_lists)  # output-->  <zip object at 0x000001B028DC4A00>
# print(list(combination_of_nested_lists))  # output-->  [(12, 15), (36, [63, 85]), ([96, 32], 49), (58, 76), (94, 25)]
# print(tuple(combination_of_nested_lists))  # output-->  ((12, 15), (36, [63, 85]), ([96, 32], 49), (58, 76), (94, 25))
# print(set(combination_of_nested_lists))  # output-->  TypeError: unhashable type: 'list'
# print(dict(combination_of_nested_lists))  # output-->  TypeError: unhashable type: 'list'

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


# def ticket_collector(func):
#
#     print("here ticket collector asked please show your ticket")
#     func()
#     print("Now ticket collector told you can go")
#
#
# def person_1():
#
#     # print("here ticket collector asked please show your ticket")
#     print("person_1 shows his ticket")
#     # print("Now ticket collector told you can go")
#
#
# def person_2():
#
#     # print("here ticket collector asked please show your ticket")
#     print("person_2 shows his ticket")
#     # print("Now ticket collector told you can go")


# person_1()
# print("--------------------------------------------------------------------------------------")
# person_2()
# print("--------------------------------------------------------------------------------------")
# ticket_collector(person_1)
# print("--------------------------------------------------------------------------------------")
# ticket_collector(person_2)
# print("--------------------------------------------------------------------------------------")

# ---------------------------------------------------------------------------------------------------------------------


# def cinemahall(func):
#
#     def ticket_collector():
#         print("here ticket collector asked please show your ticket")
#         func()
#         print("Now ticket collector told you can go")
#     return ticket_collector
#
#
# @cinemahall
# def person_1():
#
#     # print("here ticket collector asked please show your ticket")
#     print("Sumanth shows his ticket")
#     # print("Now ticket collector told you can go")
#
#
# @cinemahall
# def person_2():
#
#     # print("here ticket collector asked please show your ticket")
#     print("Mahesh shows his ticket")
#     # print("Now ticket collector told you can go")
#
#
# # cinemahall(person_1())  # not a valid one --> Sumanth shows his ticket
# # ch = cinemahall(person_1)  # valid
# # ch()  # valid
# # print("--------------------------------------------------------------------------------------")
# # ch_2 = cinemahall(person_2)  # valid
# # ch_2()  # valid
# print("--------------------------------------------------------------------------------------")
# person_1()
# print("--------------------------------------------------------------------------------------")
# person_2()


# ---------------------------------------------------------------------------------------------------------------------

def calling():

    yield 1
    yield 2
    yield 3
    yield 4


call = calling()
print(call)
print(next(call))
print(next(call))
print(next(call))
print(next(call))
# print(next(call))

# two_power_nums = [2 ** x for x in range(1, 10)]
# print(f"The list of two power nums are : {two_power_nums}")
#
# square_of_nums = [x ** 2 for x in range(1, 10)]
# print(f"The list of square of nums are {square_of_nums}")
