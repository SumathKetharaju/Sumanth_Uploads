class Laptop:

    USERNAME = "Sumanth"

    def __init__(self, name, os):
        self.name = name
        self.os = os

    @staticmethod
    def cat_project():
        return f"it is related to mining project"


lp = Laptop("DEll", "Windows")
print(f"lp.USERNAME --> {lp.USERNAME}")
print(f"lp.__dict__ --> {lp.__dict__}", "\n")

print(f"Laptop.USERNAME --> {Laptop.USERNAME}")
print(f"Laptop.__dict__ --> {Laptop.__dict__}", "\n")

lp.USERNAME = "Ravindra"
print(f"lp.USERNAME  after changing that using object --> {lp.USERNAME}")
print(f"lp.__dict__ after changing that using object --> {lp.__dict__}", "\n")

Laptop.USERNAME = "Sunil"
print(f"Laptop.USERNAME after changing that using class name --> {Laptop.USERNAME}")
print(f"Laptop.__dict__ after changing that using class name --> {Laptop.__dict__}", "\n")

print(Laptop.cat_project())
print(lp.cat_project())
print(lp.USERNAME)
print(Laptop.USERNAME)

lp_2 = Laptop("Lenovo", "Windows")
print(lp_2.USERNAME)
