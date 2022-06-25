def count_of_a_num(iterable, sample_num):

    if type(iterable) == list or type(iterable) == tuple or type(iterable) == str:
        count = 0
        for num in iterable:
            if num == sample_num:
                count += 1
        print(f"Count of a Given Item {sample_num} is --> {count}")


count_of_a_num([1, 25, 63, 98, 45, 45, "Sumanth"], "Sumanth")
count_of_a_num((1, 25, 63, 98, 45, 45, "Sumanth"), 45)
count_of_a_num("Sumanthu", "u")

