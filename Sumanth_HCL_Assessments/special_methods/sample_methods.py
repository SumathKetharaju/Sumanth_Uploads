class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.full_name()}, {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee("Sumanth", "Ketha", 50000)
emp_2 = Employee("Mahesh", "Babu", 60000)

print(emp_1)
print(emp_2)

print(repr(emp_1))
print(repr(emp_2))
print(str(emp_1))
print(str(emp_2))


print(emp_1.__repr__())
print(emp_2.__repr__())
print(emp_1.__str__())
print(emp_2.__str__())


print(1 + 2)
print("a" + "b")

print(int.__add__(1, 2))
print(emp_1 + emp_2)

print(len("text"))
print("text".__len__())

print(len(emp_1))
print(len(emp_2))
