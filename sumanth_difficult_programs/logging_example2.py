import logging

logging.basicConfig(filename="employee.log", level=logging.INFO, format="%(levelname)s : %(message)s")


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        # print(f"Created Employee : {self.first} - {self.last}")
        logging.info(f"Created Employee : {self.first} - {self.last}")

    @property
    def name(self):
        return f"{self.first}.{self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"


employee_1 = Employee("sumanth", "ketharaju")
employee_2 = Employee("sunil", "pamujula")
employee_3 = Employee("sudheer", "pamujula")
employee_4 = Employee("Ravindra", "ketharaju")
# print(employee_1.name)
# print(employee_1.email)
# print(employee_2.name)
# print(employee_2.email)
