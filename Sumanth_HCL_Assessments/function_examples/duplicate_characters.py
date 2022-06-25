def duplicate(iterable):
    if type(iterable) == list or type(iterable) == tuple:
        count_of_num = {}
        for num in iterable:
            if num not in count_of_num:
                count_of_num[num] = 1
            else:
                count_of_num[num] += 1
        print(f"Count of each num is --> {count_of_num}")
        print(f"duplicate characters are --> ", end=" ")
        for key, value in count_of_num.items():
            if value > 1:
                print(key, end=" ")
        print()
        print(f"Unique characters are --> ", end=" ")
        for key, value in count_of_num.items():
            if value == 1:
                print(key, end=" ")
        print()
    else:
        print(f"your entered incorrect data that is in format of {type(iterable)} like {iterable}, So please enter valid list or tuple")


duplicate([1, 21, 1, 21, 1, 87, 96])
# duplicate({1, 21, 1, 21, 1, 87, 96})

