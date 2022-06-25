def factors_of_num(sample_num):

    print(f"The factors of Given number {sample_num} is --> ")
    if type(sample_num) == int:
        for num in range(1, sample_num + 1):
            if sample_num % num == 0:
                print(num)
    else:
        print(f"Given number is not an integer, that is in format of {type(sample_num)}, so please enter valid integer")


number = 320
factors_of_num(number)
factors_of_num(52)
factors_of_num(52.2)

# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221]

# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))

# display the result
print("Numbers divisible by 13 are",result)
