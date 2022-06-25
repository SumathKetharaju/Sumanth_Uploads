class Father:

    WHO = "Man"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def hobbies(self):
        return f"{self.name} passion is listening songs"

    def work(self):
        return f"{self.name} is selling clothes to the customers"

    def property(self):
        return f"{self.name} is having 2acre land"

    def __repr__(self):
        return "This is a Father class"


class Mother:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def hobbies(self):
        return f"{self.name} passion is watching Movies"

    def his_work(self):
        return f"{self.name} is cooking for family members"

    def property(self):
        return f"{self.name} is having 3acre land"

    def __repr__(self):
        return "This is a Mother class"


class Son(Mother, Father):

    WHO = "Man"

    def __init__(self, name, age, gender, degree):
        super().__init__(name, age, gender)
        self.degree = degree

    def hobbies(self):
        return f"{self.name} passion is studying new technologies"

    def job(self):
        return f"{self.name} working as a software engineer"

    def __repr__(self):
        return "This is a Son class"


father = Father("Srinivasulu", 50, "Male")
print(father, "\n")  # This is a Father class

mother = Mother("Sujatha", 45, "FeMale")
print(mother, "\n")

son = Son("Sumanth", 20, "Male", "Not bad")
print(son, "\n")  # This is a Son class

print(son.name, "\n")  # This is a Son class


print(father.hobbies())  # Srinivasulu passion is selling clothes to the customers
print(father.work(), "\n")  # Srinivasulu has land of 1 acre

print(mother.hobbies())
print(mother.his_work(), "\n")


print(son.hobbies())
print(son.property())
print(son.work())
print(son.job(), "\n")  # Sumanth has land of 1 acre