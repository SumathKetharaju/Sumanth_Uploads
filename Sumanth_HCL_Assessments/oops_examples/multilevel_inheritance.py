class GrandFather:

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
        return "This is a GrandFather class"


class Father(GrandFather):

    WHO = "Man"

    def __init__(self, name, age, gender, degree):
        super().__init__(name, age, gender)
        self.degree = degree

    def hobbies(self):
        return f"{self.name} passion is studying new technologies"

    def job(self):
        return f"{self.name} working as a software engineer"

    def __repr__(self):
        return "This is a Father class"


class Son(Father):

    WHO = "Man"

    def __init__(self, name, age, gender, degree, color):
        super().__init__(name, age, gender, degree)
        self.color = color

    def hobbies(self):
        return f"{self.name} passion is enjoying with friends"

    def job(self):
        return f"{self.name} is not working"

    def __repr__(self):
        return "This is a Son class"


grandfather = GrandFather("Srinivasulu", 50, "Male")
print(grandfather, "\n")  # This is a Father class

print(grandfather.name, "\n")

father = Father("Sumanth", 20, "Male", "Not bad")
print(father, "\n")  # This is a Son class

print(father.name, "\n")  # This is a Son class

son = Son("Sumanth", 20, "Male", "Not bad", "White")

print(son.hobbies())  # Srinivasulu passion is selling clothes to the customers
print(son.work(), "\n")  # Srinivasulu has land of 1 acre


