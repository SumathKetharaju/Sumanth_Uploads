class Father:

    WHO = "Man"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hobbies(self):
        return f"{self.name} passion is listening songs"

    def work(self):
        return f"{self.name} is selling clothes to the customers"

    def property(self):
        return f"{self.name} is having 5acre land"

    def __repr__(self):
        return "This is a Father class"


class Mother:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def work(self):
        return f"{self.name} is cooking food to their family"

    def property(self):
        return f"{self.name} is having 3acre land"

    def __repr__(self):
        return "This is a Mother class"


class Son(Mother, Father):

    def __init__(self, name, age, gender, degree):
        super().__init__(name, age, gender)
        self.degree = degree

    def hobbies(self):
        return f"{self.name} passion is reading books"

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
print(f"father.property() --> {father.property()}")
print(f"father.work() --> {father.work()}", "\n")

print("---------------------------------------Mother Details------------------------------------------------")
mother = Mother("Sujatha", 45, "Female")
print(f"mother --> {mother}")
# print(f"mother.WHO --> {mother.WHO}")
print(f"mother.name --> {mother.name}")
print(f"mother.age --> {mother.age}")
print(f"mother.gender --> {mother.gender}")
print(f"mother.property() --> {mother.property()}")
print(f"mother.work() --> {mother.work()}", "\n")


print("---------------------------------------Son Details------------------------------------------------")
son = Son("Sumanth", 20, "Male", "Btech")
print(f"son --> {son}")
print(f"son.WHO --> {son.WHO}")
print(f"son.name --> {son.name}")
print(f"son.age --> {son.age}")
print(f"son.gender --> {son.gender}")
print(f"son.hobbies() --> {son.hobbies()}")
print(f"son.job() --> {son.job()}")
print(f"son.work() --> {son.work()}")
print(f"son.property() --> {son.property()}")
print(f"son.work() --> {son.work()}", "\n")

print("---------------------------------------Checking------------------------------------------------")
print(f"issubclass(Son, Father) --> {issubclass(Son, Father)}")
print(f"issubclass(Son, Mother) --> {issubclass(Son, (Father, Mother))}")
print(f"issubclass(Son, (Father, Mother)) --> {issubclass(Son, (Father, Mother))}")
print(f"Son.__mro__ --> {Son.__mro__}")
print(f"Son.mro() --> {Son.mro()}")
