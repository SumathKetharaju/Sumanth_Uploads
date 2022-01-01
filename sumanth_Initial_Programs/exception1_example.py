# DIGIT_MAP = {
#     "zero": '0',
#     "one": '1',
#     "two": '2',
#     "three": '3',
#     "four": '4',
#     "five": '5',
#     "six": '6',
#     "seven": '7'
# }
#
#
# def convert(s):
#
#     #x = -1
#     try:
#         number = ''
#         for token in s:
#             number += DIGIT_MAP[token]
#         x = int(number)
#         print(f"conversion success x={x}")
#         return int(number)
#     except (KeyError, TypeError) as e:
#         print(f"conversion error:{e!r}")
#         # x = -1
#         raise
#     finally:
#         print("Resources closed")
#
#
# convert("one three three seven".split())
#
# #convert("one three double".split())
#
# convert(512)

x = int(input("Enter a number: "))

try:
    if x % 2 == 0:
        print("operation open")
        print(f"operation success x = {x}")
    else:
        pass
except KeyError as e:
    print(f"operation fails:{e!r}")
    raise
finally:
    print("operation closed")



















