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
        return f"{self.name} is having 10acre land"

    def __repr__(self):
        return "This is a Father class"


class Father(GrandFather):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def work(self):
        return f"{self.name} is a civil engineer"

    def property(self):
        return f"{self.name} is having 3acre land"

    def __repr__(self):
        return "This is a Mother class"


class BigFather(GrandFather):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def hobbies(self):
        return f"{self.name} passion is reading books"

    def job(self):
        return f"{self.name} working as a software engineer"

    def __repr__(self):
        return "This is a Big father class"


class Son(BigFather, Father):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        # self.degree = degree

    def hobbies(self):
        return f"{self.name} passion is reading books"

    def study(self):
        return f"{self.name} studying Btech"

    def __repr__(self):
        return "This is a Son class"


print("---------------------------------------GrandFather Details------------------------------------------------")
grandfather = GrandFather("Srinivasulu", 60, "Male")
print(f"grandfather --> {grandfather}")
print(f"grandfather.WHO --> {grandfather.WHO}")
print(f"grandfather.name --> {grandfather.name}")
print(f"grandfather.age --> {grandfather.age}")
print(f"grandfather.hobbies() --> {grandfather.hobbies()}")
print(f"grandfather.property() --> {grandfather.property()}")
print(f"grandfather.work() --> {grandfather.work()}", "\n")

print("---------------------------------------Father Details------------------------------------------------")
father = Father("Sumanth", 40, "Male")
print(f"father --> {father}")
print(f"father.WHO --> {father.WHO}")
print(f"father.name --> {father.name}")
print(f"father.age --> {father.age}")
print(f"father.gender --> {father.gender}")
print(f"father.hobbies() --> {father.hobbies()}")
print(f"father.property() --> {father.property()}")
print(f"father.work() --> {father.work()}", "\n")

print("---------------------------------------BigFather Details------------------------------------------------")
big_father = BigFather("Ravindra", 43, "Male")
print(f"big_father --> {big_father}")
print(f"big_father.WHO --> {big_father.WHO}")
print(f"big_father.name --> {big_father.name}")
print(f"big_father.age --> {big_father.age}")
print(f"big_father.gender --> {big_father.gender}")
print(f"big_father.hobbies() --> {big_father.hobbies()}")
print(f"big_father.property() --> {big_father.property()}")
print(f"big_father.work() --> {big_father.work()}", "\n")

print("---------------------------------------Son Details------------------------------------------------")
son = Son("Mahesh", 20, "Male")
print(f"son --> {son}")
print(f"son.WHO --> {son.WHO}")
print(f"son.name --> {son.name}")
print(f"son.age --> {son.age}")
print(f"son.gender --> {son.gender}")
print(f"son.hobbies() --> {son.hobbies()}")
print(f"son.study() --> {son.study()}")
print(f"son.work() --> {son.work()}")
print(f"son.property() --> {son.property()}")
print(f"son.job() --> {son.job()}", "\n")

print("---------------------------------------Checking------------------------------------------------")
print(f"issubclass(Father, GrandFather) --> {issubclass(Father, GrandFather)}")
print(f"issubclass(BigFather, GrandFather) --> {issubclass(BigFather, GrandFather)}")
print(f"issubclass(Son, Father) --> {issubclass(Son, Father)}")
print(f"issubclass(Son, BigFather) --> {issubclass(Son, (Father, BigFather))}")
print(f"issubclass(Son, (BigFather, Father)) --> {issubclass(Son, (BigFather, Father))}")
print(f"Father.__mro__ --> {Father.__mro__}")
print(f"BigFather.__mro__ --> {BigFather.__mro__}")
print(f"Son.__mro__ --> {Son.__mro__}")
print(f"Son.mro() --> {Son.mro()}")
print(f"Father.mro() --> {Father.mro()}")
print(f"GrandFather.mro() --> {GrandFather.mro()}")
