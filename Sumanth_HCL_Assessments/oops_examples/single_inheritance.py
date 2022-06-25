class Father:

    WHO = "Man"

    def __init__(self, name, age, gender, behaviour):
        self.name = name
        self.age = age
        self.gender = gender
        self.behaviour = behaviour

    def hobbies(self):
        return f"{self.name} passion is listening songs"

    def work(self):
        return f"{self.name} is selling clothes to the customers"

    def __repr__(self):
        return "This is a Father class"


class Son(Father):

    WHO = "Man"

    def __init__(self, name, age, gender, behaviour, color):
        super().__init__(name, age, gender, behaviour)
        self.color = color

    def hobbies(self):
        return f"{self.name} passion is watching movies"

    def job(self):
        return f"{self.name} working as a software engineer"

    def __repr__(self):
        return "This is a Son class"


father = Father("Srinivasulu", 50, "Male", "Good")
print(father)  # This is a Father class
son = Son("Sumanth", 20, "Male", "Not bad")
print(son)  # This is a Son class
print(son.name)  # This is a Son class

print(father.hobbies())  # Srinivasulu passion is selling clothes to the customers
print(father.work())  # Srinivasulu has land of 1 acre


print(son.hobbies())  # Sumanth passion is watching movies
print(son.job())  # Sumanth has land of 1 acre


