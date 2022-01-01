# import itertools,random
# import calendar
"""24.Python program to display powers of 2 by using anonymous function"""
# terms = 8
# # terms = int(input("How many terms you get: "))
# result = list(map(lambda x: 2 ** x, range(terms)))
# print("The total terms are: ")
# for i in range(terms):
#     print("2 is raised to power of", i, "is", result[i])

"""25.Python program to find number divisible by another number"""
# my_list = [12, 24, 32, 60, 84, 57, 72, 108, 120]
# result = list(filter(lambda x: x % 12 == 0, my_list))
# print(result)

"""26.Python program to to convert decimal to binary, octal, hexadecimal"""
# dec = 8
# print("The decimal of", dec)
# print("in binary is", bin(dec))
# print("in octal is", oct(dec))
# print("in hexadecimal is", hex(dec))

"""27.Python program to find the Ascii value of a character"""
# c = "p"
# d = "112"
# print("The Ascii value of '" + c + "' is", ord(c))
# print("The Ascii value of '" + d + "' is", chr(int(d)))

"""28.Python program to find the factors of number"""


# def print_factors(x):
#
#     print("The factors of", x, "are:")
#     for i in range(1, x + 1):
#         if x % i == 0:
#             print(i)
#
#
# num = 32
# print_factors(num)

"""29.Python program to find gcd or hcf of two numbers using for loop"""


# def compute_hcf(x, y):
#
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if (x % i == 0) and (y % i == 0):
#             hcf = i
#     return hcf
#
#
# num1 = 54
# num2 = 24
# hcf = compute_hcf(num1, num2)
# print("The hcf  of two numbers is", hcf)

"""30.Python program to find gcd or hcf of two numbers using formulae"""


# def compute_hcf(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
#
# num1 = 54
# num2 = 20
# print("The H.C.F is:", compute_hcf(num1, num2))

"""31.Python program to find the L.C.M of two numbers using for loop"""


# def compute_lcm(x, y):
#
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while True:
#         if greater % x == 0 and greater % y == 0:
#             lcm = greater
#             break
#         greater += 1
#     return lcm
#
#
# print("The L.C.M is: ", compute_lcm(54, 24))

"""32.Python program to find the L.C.M of two numbers using g.c.d"""


# def compute_gcd(x, y):
#
#     while y:
#         x, y = y, x % y
#     return x
#
#
# def compute_lcm(x, y):
#
#     lcm = x * y / compute_gcd(x, y)
#     return lcm
#
#
# print("The L.C.M is: ", compute_lcm(54, 24))

"""33.Python program to make a simple calculator"""


# def add(x, y):
#     return x + y
#
#
# def subtract(x, y):
#     return x - y
#
#
# def multiply(x, y):
#     return x * y
#
#
# def divide(x, y):
#     return x / y
#
#
# print("select operation")
# print("1.Add")
# print("2.subtract")
# print("3.multiply")
# print("4.divide")
#
# while True:
#     choice = input("Enter the choice 1/2/3/4: ")
#     if choice in ("1", "2", "3", "4"):
#         num1 = int(input("Enter first number:"))
#         num2 = int(input("Enter second number:"))
#
#         if choice == "1":
#             print(num1, "+", num2, "is", add(num1, num2))
#
#         if choice == "2":
#             print(num1, "-", num2, "is", subtract(num1, num2))
#
#         if choice == "3":
#             print(num1, "*", num2, "is", multiply(num1, num2))
#
#         if choice == "4":
#             print(num1, "/", num2, "is", divide(num1, num2))
#         break
#     else:
#         print("Invalid input")

"""34.Python program to shuffle deck of cards"""

# deck_of_cards = list(itertools.product(range(1, 14), ["Heart", "Diamond", "spade", "club"]))
# random.shuffle(deck_of_cards)
# print("you got:")
# for i in range(5):
#     print(deck_of_cards[i][0], "of", deck_of_cards[i][1])

"""35.Python program to display calender"""
# yy = 2021
# mm = 6
# print(calendar.month(yy, mm))

"""36.Python program to display fibonacci sequence using recursion"""


# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return recur_fibo(n-1) + recur_fibo(n-2)
#
#
# print("The fibonacci sequence are: ")
# nterms = 10
# if nterms <= 0:
#     print("Enter positive integer")
# else:
#     for i in range(nterms):
#         print(recur_fibo(i))

"""37.Python program to find factorial of number using recursion"""


# def recur_factorial(n):
#
#     if n == 1:
#         return n
#     else:
#         return n * recur_factorial(n-1)
#
#
# num = 0
# if num < 0:
#     print("Enter a positive number")
# elif num == 0:
#     print("factorial of 0 is 1")
# else:
#     print(recur_factorial(num))

"""38.Python program to find sum of natural numbers using recursion"""


# def recur_sum(n):
#
#     if n <= 1:
#         return n
#     else:
#         return n + recur_sum(n-1)
#
#
# num = 5
# if num < 0:
#     print("Enter a positive number")
# else:
#     print("The sum is", recur_sum(num))

"""39.Python program to convert decimal to binary using recursion"""


def converttobinary(n):

    if n > 1:
        converttobinary(n // 2)
    print(n % 2, end=" ")


dec = 4

converttobinary(dec)
print()


