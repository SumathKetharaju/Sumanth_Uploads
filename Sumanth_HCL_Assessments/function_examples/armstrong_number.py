def armstrong_number(num):

    if type(num) == int:
        order_of_num = len(str(num))
        count_of_num = 0
        temparary_num = num

        while temparary_num > 0:
            each_digit_of_that_num = temparary_num % 10
            count_of_num += each_digit_of_that_num ** order_of_num
            temparary_num //= 10

        if count_of_num == num:
            print(f"Given Number {num} is a armstrong number")
        else:
            print(f"Given Number {num} is not a armstrong number")
    else:
        print(f"your entered Number is not an integer, that is in {type(num)} format, so please enter integer")


armstrong_number(153)
armstrong_number(1634)
armstrong_number(15)
armstrong_number(15.9)


