input_num = int(input("Enter a number: "))

for num in range(2, input_num):
    if input_num % num == 0:
        print(f"{input_num} is not a prime number")
        break
else:
    print(f"{input_num} is a prime number")
