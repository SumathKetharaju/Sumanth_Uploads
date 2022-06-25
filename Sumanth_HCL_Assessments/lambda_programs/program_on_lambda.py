print("\n---------------------------------Operations on a number using lambda--------------------------------------\n")

square_of_num = lambda x: x * x
print(f"Square of a number using 'square_of_num = lambda x: x * x' and square_of_num(8) is --> {square_of_num(8)}\n")

addition_of_num = lambda x: x + x
print(f"Addition of a number using 'addition_of_num = lambda x: x + x' and addition_of_num(10) is --> {addition_of_num(10)}\n")

division_of_num = lambda x: x // x
print(f"Division of a number using 'division_of_num = lambda x: x // x' and division_of_num(10) is --> {division_of_num(8)}\n")

remainder_of_num = lambda x: x % 2
print(f"The remainder of number using 'remainder_of_num = lambda x: x % 2' and remainder_of_num(15) is {remainder_of_num(15)}")

print("\n--------------------------------Operations on two numbers using lambda------------------------------------\n")

addition_of_two_nums = lambda x, y: x+y
print(f"The sum of two numbers using 'addition_of_two_nums = lambda x, y: x+y' and "
      f"addition_of_two_nums(20, 30) is --> {addition_of_two_nums(20, 30)}\n")

subtraction_of_two_nums = lambda x, y: x-y
print(f"The subtraction of two numbers using 'addition_of_two_nums = lambda x, y: x+y' and "
      f"subtraction_of_two_nums(50, 30) is --> {subtraction_of_two_nums(50, 30)}\n")

multiplication_of_two_nums = lambda x, y: x*y
print(f"The multiplication of two numbers using 'multiplication_of_two_nums = lambda x, y: x*y' and "
      f"multiplication_of_two_nums(5, 3) is --> {multiplication_of_two_nums(5, 3)}\n")

division_of_two_nums = lambda x, y: x/y
print(f"The division of two numbers using 'division_of_two_nums = lambda x, y: x/y' and "
      f"division_of_two_nums(15, 3) is --> {division_of_two_nums(15, 3)}\n")

print("\n--------------------------------Operations on iterable using lambda and map -------------------------------\n")

input_list = [12, 56, 89, 47, 23, 32, 24]

print(f"Given input list is --> {input_list}\n")

addition_of_list_of_nums_with_10 = list(map(lambda x: x + 10, input_list))
print(f"Applying addition to The list of numbers with 10 using "
      f"'addition_of_list_of_nums_with_10 = list(map(lambda x: x + 10, input_list))' are :--> {addition_of_list_of_nums_with_10}\n")

subtraction_of_list_of_nums_with_10 = list(map(lambda x: x - 10, input_list))
print(f"Applying subtraction to The list of numbers with 10 using "
      f"'subtraction_of_list_of_nums_with_10 = list(map(lambda x: x - 10, input_list))' are :--> {subtraction_of_list_of_nums_with_10}\n")

multiplication_of_list_of_nums_with_2 = list(map(lambda x: x * 2, input_list))
print(f"Applying multiplication to The list of numbers with 10 using "
      f"'multiplication_of_list_of_nums_with_2 = list(map(lambda x: x * 2, input_list))' are :--> {multiplication_of_list_of_nums_with_2}\n")

division_of_list_of_nums_with_2 = list(map(lambda x: x / 2, input_list))
print(f"Applying division to The list of numbers with 2 using "
      f"'division_of_list_of_nums_with_2 = list(map(lambda x: x / 2, input_list))' are :--> {division_of_list_of_nums_with_2}\n")

integer_division_of_list_of_nums_with_2 = list(map(lambda x: x // 2, input_list))
print(f"Applying integer division to The list of numbers with 2 using "
      f"'integer_division_of_list_of_nums_with_2 = list(map(lambda x: x // 2, input_list))' are :--> {integer_division_of_list_of_nums_with_2}\n")

remainders_of_list_of_nums_with_2 = list(map(lambda x: x % 2, input_list))
print(f"Applying remainder to The list of numbers with 2 using "
      f"'remainders_of_list_of_nums_with_2 = list(map(lambda x: x % 2, input_list))' are :--> {remainders_of_list_of_nums_with_2}\n")

print("\n----------------------------Operations on iterable using lambda and filter -------------------------\n")

sample_list = [12, 56, 89, 47, 23, 32, 24, 84]

print(f"Given sample list is --> {sample_list}\n")

even_nums = list(filter(lambda x: x % 2 == 0, sample_list))
print(f"To print list of even numbers we will use "
      f"'even_nums = list(filter(lambda x: x % 2 == 0, sample_list))' then it gives :--> {even_nums}\n")

odd_nums = list(filter(lambda x: x % 2 != 0, sample_list))
print(f"To print list of odd numbers we will use "
      f"'odd_nums = list(filter(lambda x: x % 2 != 0, sample_list))' then it gives :--> {odd_nums}\n")

sample_list_2 = [12, 56, 89, 47, "Sumanth", 23, 32, "HCL", 24, 84]
print(f"Given sample list is --> {sample_list_2}\n")

strings = list(filter(lambda x: type(x) == str, sample_list_2))
print(f"To print list of strings from the sample list we will use "
      f"'strings = list(filter(lambda x: type(x) == str, sample_list_2))' then it gives :--> {strings}\n")

integers = list(filter(lambda x: type(x) == int, sample_list_2))
print(f"To print list of integers we will use "
      f"'integers = list(filter(lambda x: type(x) == int, sample_list_2))' then it gives :--> {integers}\n")

print("---------------------------------------------------------------------------------------------------------")

