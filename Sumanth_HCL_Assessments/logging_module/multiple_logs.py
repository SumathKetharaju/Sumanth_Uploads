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

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("function.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiple(x, y):
    return x * y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.error("Tried to divided by Zero")
    else:
        return result


num_1 = 40
num_2 = 0

print(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
print(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
print(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
print(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")

# print("--------------------------------This is debug level-----------------------------------------------")
logger.debug(f"------------------------------ This is logging debug level ----------------------------------------")
logger.debug(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
logger.debug(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
logger.debug(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
logger.debug(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")


# print("--------------------------------This is info level-----------------------------------------------")
logger.info(f"------------------------------ This is logging Info level ----------------------------------------")
logger.info(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
logger.info(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
logger.info(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
logger.info(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")

# print("--------------------------------This is warning level-----------------------------------------------")
logger.warning(f"------------------------------ This is logging warning level ----------------------------------------")
logger.warning(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
logger.warning(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
logger.warning(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
logger.warning(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")

# print("--------------------------------This is error level-----------------------------------------------")
logger.error(f"------------------------------ This is logging error level ----------------------------------------")
logger.error(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
logger.error(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
logger.error(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
logger.error(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")

# print("--------------------------------This is critical level-----------------------------------------------")
logger.critical(f"---------------------------- This is logging critical level ------------------------------------")
logger.critical(f"The addition of two numbers {num_1} and {num_2} is --> {add(num_1, num_2)}")
logger.critical(f"The subtraction of two numbers {num_1} and {num_2} is --> {subtract(num_1, num_2)}")
logger.critical(f"The multiplication of two numbers {num_1} and {num_2} is --> {multiple(num_1, num_2)}")
logger.critical(f"The division of two numbers {num_1} and {num_2} is --> {divide(num_1, num_2)}")
