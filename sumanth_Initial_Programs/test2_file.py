"""11. Python program to check if a number is positive, negative , zero"""
# num = 9
# # num = int(input("Enter a number: "))
# if num <= 0:
#     print("negative")
# elif num == 0:
#     print("zero")
# else:
#     print("positive")

# if num >= 0:
#     if num > 0:
#         print("positive")
#     else:
#         print("zero")
# else:
#     print("Negative")

"""12.Python program to check if a number is even or odd"""
# num = 9
# # num int((input("Enter a number: ")))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

"""13.Python program to check leap year"""
# year = 2020
# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("{} is a leap year".format(year))
#         else:
#             print("{} is not a leap year".format(year))
#     else:
#         print("{} is a leap year".format(year))
# else:
#     print("{} is not a leap year".format(year))

"""14.Python program to find largest among three numbers"""
# num1 = 589
# num2 = 665
# num3 = 94
# # num1 = int(input("Enter first number: "))
# # num2 = int(input("Enter second number: "))
# # num3 = int(input("Enter third number: "))
# if num1 > num2 and num1 > num3:
#     largest = num1
# elif num2 > num3 and num2 > num1:
#     largest = num2
# else:
#     largest = num3
# print("The largest number is ", largest)
# print(largest, "is largest among three numbers")
# print("The largest number among three numbers is {}".format(largest))
# print(f"{largest} is the largest number")
# print("%.2f is largest number" % largest)

"""15.Python program to check prime number"""
# num = 1
# num = int(input("Enter a number: "))
# if num <= 1:
#     print("Prime numbers starts from 2: ")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("{} is not a prime number".format(num))
#             print(i, "times", num // i, "is equal to", num)
#             break
#     else:
#         print(f"{num} is a prime number")

"""16.Python program to print all prime numbers with in an interval"""
# lower = 2
# upper = 100
# print("prime numbers between", lower, "and", upper, "are: ")
# for num in range(lower, upper+1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

"""17.Python program to find factorial of a number"""
# num = 5
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Factorial is not exist for negative numbers")
# elif num == 0:
#     print("Factorial of 0 is 1")
# else:
#     factorial = 1
#     for i in range(1, num+1):
#         factorial = factorial * i
#     print(factorial)
#     print(f"factorial of {num} is {factorial}")
#     print("Factorial of {} is {}".format(num, factorial))

"""18.Python program to display multiplication table"""
# num = 9
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(num, "*", i, "= ", num * i)
#   #print(f"{num} * {i} = {num * i}")

"""19.Python program to print fibonacci sequence"""
# num_of_terms = 10
# # num_of_terms = int(input("Enter number of terms"))
# n1, n2 = 0, 1
# count = 0
# if num_of_terms <= 0:
#     print("Positive number")
# elif num_of_terms == 1:
#     print("fibonacci sequence upto 1 are: ")
#     print(n1)
# else:
#     print("fibonacci sequence are: ")
#     while count < num_of_terms:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1

"""20.Python program to check Armstrong number with 3 digits"""
# num = 154
# # num = int(input("Enter a number: "))
# temp = num
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if sum == num:
#     print("Given number is an armstrong number")
# else:
#     print("Given number is not an armstrong number")

"""21.Python program to check armstrong numbers with n digits"""
# num = 1545
# order = len(str(num))
# # # num = int(input("Enter a number: "))
# temp = num
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10
# if sum == num:
#     print("Given number is an armstrong number")
# else:
#     print("Given number is not an armstrong number")

"""22.Python program to display armstrong numbers with in interval"""
# lower = 1000
# upper = 3000
# print("Armstrong numbers between", lower, "and", upper, "are: ")
# for num in range(lower, upper+1):
#     order = len(str(num))
#     temp = num
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#     if sum == num:
#         print(num)

"""23.Python program to display sum of natural numbers"""
num = 3
sum = 0
print("The sum of natural numbers is: ")
for i in range(1, num+1):
    sum = sum + i
    num -= 1
print(sum)