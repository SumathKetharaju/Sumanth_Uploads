import logging


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


logging.basicConfig(filename="calc.log", level=logging.WARNING, format="%(asctime)s : %(levelname)s : %(message)s")

num1 = 10
num2 = 2

logging.warning(f"The sum is {add(num1, num2)}")
logging.warning(f"The subtraction is {subtract(num1, num2)}")
logging.warning(f"The multiplication is {multiply(num1, num2)}")
logging.warning(f"The division is {divide(num1, num2)}")
