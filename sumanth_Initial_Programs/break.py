av = 5
x = int(input("how many candles u want "))
i = 1
while i <= x:
    if i > av:
        print("out of stock")
        break
    print("candle")
    i += 1
print("bye")
