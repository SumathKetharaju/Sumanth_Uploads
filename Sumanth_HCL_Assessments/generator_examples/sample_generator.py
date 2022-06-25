def sample_gen():

    print("This is is a Sample generator")
    yield 5
    yield 6


print(f"---------------------------- Calling generator function using 'sample_gen()' --------------------------------\n")
sample_gen()

print(f"----------------------- Calling generator function using 'print(sample_gen())' -----------------------------\n")
print(f"{sample_gen()}\n")

print(f"--------------------- Creating generator object using 'gen_object = sample_gen()' --------------------------\n")
gen_object = sample_gen()

print(f"----------------------- Calling generator object using 'print(gen_object)' -----------------------------\n")
print(f"{gen_object}\n")

print(f"--------------------- Calling next generator object using 'print(next(gen_object))' -----------------------\n")
print(f"{next(gen_object)}\n")

print(f"--------------------- Calling next generator object using 'print(next(gen_object))' -----------------------\n")
print(f"{next(gen_object)}\n")

print(f"--------------------- Calling next generator object using 'print(next(gen_object))' -----------------------\n")
print(f"StopIteration")
# StopIteration
# print(next(gen_object))


def square_of_numbers(nums):
    list_of_square_of_nums = []
    for num in nums:
        list_of_square_of_nums.append(num * num)
    return list_of_square_of_nums


my_nums = square_of_numbers([2, 4, 3, 5, 9, 7])
print(my_nums)

# def square_of_numbers(nums):
#     for num in nums:
#         yield num * num
#
#
# my_nums = square_of_numbers([2, 4, 3, 5, 9, 7])
# print(my_nums)
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# for n in my_nums:
#     print(n)

# generator_comprehension = (num * num for num in [2, 4, 3, 5, 9, 7])
# print(generator_comprehension)
#
# for i in generator_comprehension:
#     print(i)

