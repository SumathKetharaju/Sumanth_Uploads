import logging

logging.basicConfig(filename="calculator.log", level=logging.INFO, format="%(asctime)s : %(levelname)s : %(message)s")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


num1 = 20
num2 = 10

logging.info(f"The Sum is : {add(num1, num2)}")
logging.info(f"The Difference is : {subtract(num1, num2)}")
logging.info(f"The Multiplication is : {multiply(num1, num2)}")
logging.info(f"The Division is : {divide(num1, num2)}")


