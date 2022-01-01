#   This is program to find out prime number

input_string = input("Enter any number u want to test?")
input_number = int(input_string)

#  17-->1, 17 , any thing other than this

count = 0

for i in range(2, input_number):
    if input_number % i == 0:
        print("This number is not prime number.")
        break
else:
    print("This is prime number.")





