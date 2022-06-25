class Father:

    WHO = "Man"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hobbies(self):
        return f"{self.name} passion is listening songs"

    def work(self):
        return f"{self.name} is selling clothes to the customers"

    def __repr__(self):
        return "This is a Father class"


class Son(Father):

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def hobbies(self):
        return f"{self.name} passion is watching movies"

    def job(self):
        return f"{self.name} working as a software engineer"

    def __repr__(self):
        return "This is a Son class"


print("---------------------------------------Father Details------------------------------------------------")
father = Father("Srinivasulu", 50)
print(f"father --> {father}")
print(f"father.WHO --> {father.WHO}")
print(f"father.name --> {father.name}")
print(f"father.age --> {father.age}")
print(f"father.hobbies() --> {father.hobbies()}")
print(f"father.work() --> {father.work()}", "\n")

print("---------------------------------------Son Details------------------------------------------------")
son = Son("Sumanth", 20, "Male")
print(f"son --> {son}")
print(f"son.WHO --> {son.WHO}")
print(f"son.name --> {son.name}")
print(f"son.age --> {son.age}")
print(f"son.gender --> {son.gender}")
print(f"son.hobbies() --> {son.hobbies()}")
print(f"son.job() --> {son.job()}")
print(f"son.work() --> {son.work()}", "\n")

print("---------------------------------------Checking------------------------------------------------")
print(f"issubclass(Son, Father) --> {issubclass(Son, Father)}")
print(f"Son.__mro__ --> {Son.__mro__}")
print(f"Son.mro() --> {Son.mro()}")
