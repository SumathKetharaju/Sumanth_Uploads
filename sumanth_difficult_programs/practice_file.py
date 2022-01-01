import itertools
import random

# input_num = int(input("Enter a number: "))
#
# if input_num > 1:
#     for num in range(2, input_num):
#         if input_num % num == 0:
#             print(f"{input_num} is not a prime number")
#             print(f"{input_num // num} times {num} is {input_num}")
#             break
#     else:
#         print(f"{input_num} is a prime number")
# else:
#     print(f"{input_num} is not a prime number")


# lower = int(input("Enter lowest number: "))
#
# upper = int(input("Enter highest number: "))
#
# print(f"The prime numbers between {lower} and {upper} are: ")
#
# for num in range(lower, upper+1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)


# input_num = int(input("Enter a number: "))
#
# factorial = 1
#
# if input_num < 0:
#     print("Enter a positive integer")
# elif input_num == 0:
#     print("Factorial of 0 is 1")
# else:
#     for num in range(1, input_num+1):
#         factorial = factorial * num
#     print(f"factorial of {input_num} is {factorial}")

# input_num = int(input("Enter a number: "))
# for num in range(1, 11):
#     print(f"{input_num} X {num} = {input_num * num}")


# nterms = int(input("Enter the nterms: "))
#
# n1 = 0
# n2 = 1
#
# count = 0
#
# if nterms <= 0:
#     print("Enter a positive integer")
# elif nterms == 1:
#     print(f"fibonacci series upto {input_num} is")
#     print(n1)
# else:
#     print("Fibonacci series are: ")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1


# input_num = int(input("Enter a number: "))
#
# sum = 0
#
# temp = input_num
#
# while temp >= 1:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
#
# if input_num == sum:
#     print(f"{input_num} is an armstrong number")
# else:
#     print(f"{input_num} is not an armstrong number")


# lower = int(input("Enter lowest number: "))
#
# upper = int(input("Enter highest number: "))
#
# print(f"The Armstrong numbers between {lower} and {upper} are: ")
#
# for num in range(lower, upper+1):
#     order = len(str(num))
#     temp = num
#     sum = 0
#     while temp >= 1:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#
#     if num == sum:
#         print(num)


# terms = int(input("Enter the terms: "))
#
# sum = 0
#
# while terms:
#     sum += terms
#     terms -= 1
# print(sum)

# input_num = int(input("Enter a number: "))
#
# if input_num < 0:
#     print("Enter a positive integer")
# else:
#     sum = 0
#     while input_num > 0:
#         sum += input_num
#         input_num -= 1
#     print(sum)


# nterms = int(input("Enter the terms: "))
#
# expected_output = list(map(lambda x: 2 ** x, range(nterms)))
#
# print(expected_output)


# input_list = [12, 53, 24, 89, 67, 16, 36, 59, 69]
#
# result = list(filter(lambda x: x % 12 == 0, input_list))
#
# print(result)

# char = "p"
#
# print(f"The ascii value of '{char}' is {ord(char)}")

# num = 112
#
# print(f"the ascii value of '{num}' is {chr(num)}")

# input_num = int(input("Enter a number: "))
#
# for num in range(1, input_num+1):
#     if input_num % num == 0:
#         print(num)

# deck_of_cards = list(itertools.product(range(1, 14), ["spade", "diamond", "club", "Heart"]))
#
# random.shuffle(deck_of_cards)
#
# print("you got 5: ")
#
# for card in range(5):
#     print(f"{deck_of_cards[card][0]} of {deck_of_cards[card][1]}")


# input_string = input("Enter a string: ")
#
# reverse_string = input_string[::-1]
#
# if input_string == reverse_string:
#     print(f"Give string {input_string} is palindrome")
# else:
#     print(f"Give string {input_string} is not palindrome")



