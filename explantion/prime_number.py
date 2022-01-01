# input_num = 5
#
# for num in range(2, input_num):
#     if input_num % num == 0:
#         print(f"{input_num} is not prime number")
#         break
# else:
#     print(f"{input_num} is prime number")

# lowest_num = 2
# highest_num = 50
# print(f"Prime numbers between {lowest_num} and {highest_num} are: ")
# for num in range(lowest_num, highest_num+1):
#     for n in range(2, num):
#         if num % n == 0:
#             break
#     else:
#         print(num)

year = 2020
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
