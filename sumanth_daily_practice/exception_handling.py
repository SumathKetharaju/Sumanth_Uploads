num = int(input("Enter a number: "))

try:
    result = 1 / num
    print(result)
except ZeroDivisionError:
    print("Num is not divided by Zero")
finally:
    print("Always executed")
