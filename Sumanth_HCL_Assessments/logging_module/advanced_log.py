import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("present_emp.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        # logging.debug(f"CreatedEmployee Full Name is --> {self.full_name()} and Email is --> {self.email()}")
        logger.debug(f"CreatedEmployee Full Name is --> {self.full_name()} and Email is --> {self.email()}")

    # @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@gmail.com"

    # @property
    def full_name(self):
        return f"{self.first_name}.{self.last_name}"


emp_1 = Employee("MaheshBabu", "Ghattamaneni")
emp_2 = Employee("TarakaRatna", "Ramarao")
emp_3 = Employee("Ram", "Charan")
