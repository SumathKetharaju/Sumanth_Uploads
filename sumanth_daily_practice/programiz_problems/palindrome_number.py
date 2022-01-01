nterms = int(input("Enter nterms: "))
n1, n2 = 0, 1

if nterms <= 0:
    print("Enter positive number")
elif nterms == 1:
    print(f"fibanacci series upto 1 is {n1}")
else:
    count = 0
    print("Fibonacci series are: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count += 1


