import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(level=logging.CRITICAL)

# logging.basicConfig(filename="first.log", level=logging.DEBUG)
# logging.basicConfig(filename="first.log", level=logging.INFO)
# logging.basicConfig(filename="first.log", level=logging.WARNING)
# logging.basicConfig(filename="first.log", level=logging.ERROR)
# logging.basicConfig(filename="first.log", level=logging.CRITICAL)

logging.basicConfig(filename="first.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiple(x, y):
    return x * y


def divide(x, y):
    return x / y


num_1 = 40
num_2 = 20

print(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
print(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
print(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
print(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")

# print("--------------------------------This is debug level-----------------------------------------------")
logging.debug(f"------------------------------ This is logging debug level ----------------------------------------")
logging.debug(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
logging.debug(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
logging.debug(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
logging.debug(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")


# print("--------------------------------This is info level-----------------------------------------------")
logging.info(f"------------------------------ This is logging Info level ----------------------------------------")
logging.info(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
logging.info(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
logging.info(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
logging.info(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")

# print("--------------------------------This is warning level-----------------------------------------------")
logging.warning(f"------------------------------ This is logging warning level ----------------------------------------")
logging.warning(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
logging.warning(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
logging.warning(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
logging.warning(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")

# print("--------------------------------This is error level-----------------------------------------------")
logging.error(f"------------------------------ This is logging error level ----------------------------------------")
logging.error(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
logging.error(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
logging.error(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
logging.error(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")

# print("--------------------------------This is critical level-----------------------------------------------")
logging.critical(f"---------------------------- This is logging critical level ------------------------------------")
logging.critical(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
logging.critical(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
logging.critical(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
logging.critical(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")
