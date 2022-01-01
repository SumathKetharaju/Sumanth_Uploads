import logging


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiple(x, y):
    return x * y


def divide(x, y):
    return x / y


logging.basicConfig(filename="file.log", level=logging.DEBUG, format="%(asctime)s : %(levelname)s : %(message)s")

num1 = 20
num2 = 5

addition_of_two_numbers = add(num1, num2)
# print(f"addition of two numbers is {addition_of_two_numbers}")
# print(f"Add : {num1} + {num2} = {addition_of_two_numbers}")
logging.debug(f"Add : {num1} + {num2} = {addition_of_two_numbers}")
# logging.warning(f"Add : {num1} + {num2} = {addition_of_two_numbers}")


subtraction_of_two_numbers = subtract(num1, num2)
# print(f"subtraction of two numbers is {subtraction_of_two_numbers}")
# print(f"subtract : {num1} - {num2} = {subtraction_of_two_numbers}")
logging.debug(f"subtract : {num1} - {num2} = {subtraction_of_two_numbers}")
# logging.warning(f"subtract : {num1} - {num2} = {subtraction_of_two_numbers}")

multiplication_of_two_numbers = multiple(num1, num2)
# print(f"multiplication of two numbers is {multiplication_of_two_numbers}")
# print(f"multiple : {num1} * {num2} = {multiplication_of_two_numbers}")
logging.debug(f"multiple : {num1} * {num2} = {multiplication_of_two_numbers}")
# logging.warning(f"multiple : {num1} * {num2} = {multiplication_of_two_numbers}")

division_of_two_numbers = divide(num1, num2)
# print(f"division of two numbers is {division_of_two_numbers}")
# print(f"divide : {num1} / {num2} = {division_of_two_numbers}")
logging.debug(f"divide : {num1} / {num2} = {division_of_two_numbers}")
# logging.warning(f"divide : {num1} / {num2} = {division_of_two_numbers}")

