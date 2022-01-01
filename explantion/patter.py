# print("Hello World")
# rows = 7
# k = rows - 1
# for r in range(0, rows):
#     if r % 2 == 0:
#         for c in range(0, k):
#             print(end=" ")
#         k = k - 2
#         for c in range(0, r+1):
#             print("* ", end="")
#         print()

rows = 7
spaces = rows - 1
for r_index in range(0, rows):
    for c_index in range(0, spaces):
        print(end=" ")
    spaces = spaces - 1
    for c_index in range(0, r_index+1):
        print("*", end=" ")
    print()

# size = 7
# m = (2 * size) - 2
# for i in range(0, size):
#     for j in range(0, m):
#         print(end=" ")
#     m = m - 1 # decrementing m after each loop
#     for j in range(0, i + 1):
#         # printing full Triangle pyramid using stars
#         print("* ", end=' ')
#     print(" ")

# j = 1
# for i in range(5, 0, -1):
#     print(" "*i, "*"*j)
#     j += 2

