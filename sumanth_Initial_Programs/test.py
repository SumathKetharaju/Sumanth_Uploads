"""1.Python program to print Hello world program"""
# print("Hello world!")
# import cmath
# import random
"""2.Python program to find sum of two numbers"""
# num1 = 89
# num2 = 56
#
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum = num1 + num2
# print(sum)
# print("The sum of", num1, "and", num2, "is:", sum)
# print("The sum of {} and {} is {}".format(num1, num2, sum))
# print(f"The sum of {num1} and {num2} is {sum}")

"""3.Python program to find square root of a number"""
# num = 89
# # num = float(input("Enter a number))
# sqrt_num = num ** 0.5
# print(sqrt_num)
# print("The square root of", num, "is: ",sqrt_num)
# print("the square root of {} is {}".format(num, sqrt_num))
# print(f"The square root of {num} is {sqrt_num}")
# print("The square root of %0.3f is %0.3f" % (num, sqrt_num))

"""4.Python program to find the square root of a complex number"""

# num = 1 + 5j
# num = eval(input("Enter a number: "))
# num_sqrt = cmath.sqrt(num)
# print(num_sqrt.real, num_sqrt.imag)
# print("The square root of", num, "is: ", num_sqrt.real, num_sqrt.imag)
# print("The square root of {0} is {1:0.3f} and {2:0.3f}".format(num, num_sqrt.real, num_sqrt.imag))
# print(f"The square root of {num} is {num_sqrt.real, num_sqrt.imag}")
# print("%0.3f and %0.3f are the square root of num " % (num_sqrt.real,num_sqrt.imag))

"""5.Python program to calculate the area of triangle"""
# a = 86
# b = 58
# c = 98
# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))
# s = a + b + c / 2
# area_of_triangle = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print(area_of_triangle)
# print("Area of triangle is", area_of_triangle)
# print("{0:.2f} is the Area of triangle".format(area_of_triangle))
# print(f"Area of triangle is {area_of_triangle}")
# print("%.2f is the area of triangle" % area_of_triangle)

"""6.Python program to solve quadratic equation"""
# a = 1
# b = 5
# c = 6
# a = float(input("Enter a first number:"))
# b = float(input("Enter a second number:"))
# c = float(input("Enter a third number:"))
# d = (b ** 2) - (4 * a * c)
# sol1 = ((-b + cmath.sqrt(d)) / 2 * a)
# sol2 = ((-b - cmath.sqrt(d)) / 2 * a)
# print(sol1, sol2)
# print("The solutions are", sol1, sol2)
# print("The solutions are {0} and {1}".format(sol1.real, sol2.imag))
# print(f"The solutions are {sol1.real} and {sol2.imag}")
# print("%0.2f and %0.2f are solutions of quadratic equation" % (sol1,sol2)

"""7.Python program to swap two variables"""
# x = 8
# y = 4
# print("x and y before swapping are: ")
# print(x)
# print(y)
# print("x and y after swapping are: ")
# temp = x
# x = y
# y = temp
# x, y = y, x
# x = x + y
# y = x - y
# x = x - y
# x = x * y
# y = x / y
# x = x / y
# x = x ^ y
# y = x ^ y
# x = x ^ y
# print(x)
# print(y)

"""8.Python program to generate a random number"""
# print(random.randint(5, 55))

"""9. Python program to convert kilometers to miles"""
# kilometers = 82
# kilometers = int(input("Enter a number in kilometers: "))
# conv_fac = 0.621371
# miles = conv_fac * kilometers
# print(miles)
# print(kilometers, "kilometers is equal to the", miles, "miles")
# print("{0:.2f} kilometers is equal to the {1} miles".format(kilometers, miles))
# print(f"{kilometers} kilometers is equal to the {miles} miles")
# print("%0.2f kilometers is equal to the %0.2f miles" % (kilometers, miles))

"""10. Python program to convert celsius to fahreheit"""
# celsius = 22.3
celsius = float(input("Enter a number in celsius: "))
# celsius * 1.8 = fahrenheit - 32
fahrenheit = (celsius * 1.8) + 32
print(fahrenheit)
print(celsius, "celsius is equal to the", fahrenheit, "fahrenheit")
print("{} celsius is equal to the {} fahrenheit".format(celsius, fahrenheit))
print(f"{celsius} celsius is equal to the {fahrenheit} fahrenheit")
print("%0.2f celsius is equal to the %0.2f fahrenheit" % (celsius, fahrenheit))
