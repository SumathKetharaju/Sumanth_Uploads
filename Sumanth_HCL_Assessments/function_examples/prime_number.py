def prime_number(input_num):

    if input_num > 0:

        for num in range(2, input_num):
            if input_num % num == 0:
                # print(f"{input_num} is not a prime number")
                return f"your entered number is {input_num}, that is not a prime number"
                # break
        else:
            # print(f"{input_num} is prime number")
            return f"your entered number is {input_num}, yes that is a prime number"
    else:
        # print("enter a valid number")
        return f"your entered number is {input_num}, Please enter a Positive number"


print(prime_number(3))
print(prime_number(0))
print(prime_number(15))

list_of_prime_numbers = []
list_of_not_prime_numbers = []


def prime_numbers_list(input_list):

    if type(input_list) == list:

        for input_num in input_list:

            if input_num > 0:

                for num in range(2, input_num):
                    if input_num % num == 0:
                        list_of_not_prime_numbers.append(input_num)
                        # print(f"{input_num} is not a prime number")
                        # return f"your entered number is {input_num}, that is not a prime number"
                        break
                else:
                    # print(f"{input_num} is prime number")
                    list_of_prime_numbers.append(input_num)
                    # return f"your entered number is {input_num}, yes that is a prime number"
            else:
                # print("enter a valid number")
                list_of_not_prime_numbers.append(input_num)
                # return f"your entered number is {input_num}, Please enter a Positive number"
    else:
        print(f"Your entered input is not in the list format, that is in the format of {type(input_list)}")


sample_list = [2, 12, 3, 58, 64, 7, 9, 0, 52, 11]
prime_numbers_list(sample_list)
print(f"List of Prime numbers are --> {list_of_prime_numbers}")
print(f"List of other numbers are --> {list_of_not_prime_numbers}")
# print(list_of_not_prime_numbers)

