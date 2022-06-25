import threading
import time


def square_of_nums(n):

    result = n * n
    print(f"The Square Given number {n} is --> {result}")


input_list = [2, 12, 3, 13, 5, 15]
square_nums = []

for num in input_list:
    # square_of_nums(n)
    # square_nums.append(result)
    thread_1 = threading.Thread(target=square_of_nums, args=(num, ))
    square_nums.append(thread_1)

    thread_1.start()
    thread_1.join()

# thread_1 = threading.Thread(target=square_of_nums, args=(12, 14))
# thread_1.start()
# thread_1.join()
# square_nums.append(thread_1)


# print(square_nums)

