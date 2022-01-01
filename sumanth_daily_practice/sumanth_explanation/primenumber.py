""" Python program to check whether student got good marks or passed or failed """
# input_marks = int(input("Enter your marks: "))
# if input_marks <= 100:
#     if input_marks > 90:
#         print("You achieved good marks")
#     elif input_marks > 40:
#         print("you are passed")
#     else:
#         print("you are failed")
# else:
#     print("Not valid")

""" Python program to print range of numbers """
# for num in range(1, 11):
#     print(num)

""" Python program to print particular range of numbers """
# for num in range(1, 11):
#     if num == 6:
#         break
#     print(num)

""" Python program to check how else statement is executed for 'for' loop """
# for num in range(1, 11):
#     print(num)
# else:
#     print("This else statement is executed after for loop executed completely")

""" Python program to check how else statement is executed for 'for' loop If it contains 'if' condition """
# for num in range(1, 11):
#     if num == 5:
#         print(num)
#         break
# else:
#     print("'if condition' is True This else statement is Never Executed")

""" Python program to check how else statement is executed for 'for' loop If it contains 'if' condition """
# for num in range(1, 11):
#     if num == 11:
#         print(num)
#         break
# else:
#     print("'if condition' is False This else statement is Executed")

""" Python program to check whether prime number or not """
# input_num = 0
# if input_num > 1:
#     for num in range(2, input_num):
#         if input_num % num == 0:
#             print(f"{input_num} is not a prime number")
#             break
#     else:
#         print(f"{input_num} is a prime number")
# else:
#     print(f"{input_num} is not a prime number")

""" Python program to check whether prime number or not """
# least_num = int(input("Enter least_num number: "))
# highest_num = int(input("Enter highest_num number: "))
#
# for num in range(least_num, highest_num+1):
#     if num > 1:
#         for n in range(2, num):
#             if num % n == 0:
#                 break
#         else:
#             print(num)

""" Python program to print names """
# input_list = ["Visweswar", "Mahesh", "Avinash", "Bharat"]
# for index in input_list:
#     print(index)

""" Python program to print names in another way"""
# input_list = ["Visweswar", "Mahesh", "Avinash", "Bharat"]
# for name in range(len(input_list)):
#     print(input_list[name])

""" Python program to print names in reverse order"""
input_list = ["Visweswar", "Mahesh", "Avinash", "Bharat"]
for index in range(len(input_list)-1, -1, -1):
    print(input_list[index])
