for row in range(5):
    for column in range(row+1):
        print("*", end=" ")
    print()

print("---------------------------------------------------------------------------------------")

for row in range(5, -1, -1):
    for column in range(row):
        print("*", end=" ")
    print()

print("---------------------------------------------------------------------------------------")
for row in range(8):
    if row % 2 == 0:
        for column in range(row+1):
            print("*", end=" ")
        print()

print("---------------------------------------------------------------------------------------")

for row in range(8, -1, -1):
    if row % 2 == 0:
        for column in range(row-1):
            print("*", end=" ")
        print()


