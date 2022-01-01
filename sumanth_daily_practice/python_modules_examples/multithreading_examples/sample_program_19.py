import threading


def divide_by_12(num):

    sample_list = []
    for num in range(1, 100):
        if num % 12 == 0:
            sample_list.append(num)

    print(f"numbers Divisible by 12 are {sample_list}")


def divide_by_11(num):

    sample_list_1 = []
    for num in range(1, 100):
        if num % 11 == 0:
            sample_list_1.append(num)
    print(f"numbers Divisible by 11 are {sample_list_1}")


d_1 = threading.Thread(target=divide_by_12, args=("i",))
d_2 = threading.Thread(target=divide_by_11, args=("j",))

d_1.start()
d_2.start()

d_1.join()
d_2.join()

print("Success")

