class Father:

    WHO = "MAN"

    def __init__(self, name, age):
        self.name = name
        self.ages = age
        self.behaviour = "good"

    def method_1(self):
        print(f"This is method1 calling name {self.name} in print statement")

    def method_2(self):
        return f"This is method2 calling age {self.ages} in return statement"

    @classmethod
    def method_3(cls):
        # NameError: name 'self' is not defined
        # return f"This is class method calling instance variable age {self.ages} in return statement"

        # AttributeError: type object 'Father' has no attribute 'ages'
        # return f"This is class method calling instance variable age {cls.ages} in return statement"

        return f"This is method3 calling class variable {cls.WHO} in return statement"

    @staticmethod
    def method_4(sex):
        # NameError: name 'self' is not defined
        # return f"This is static method calling instance variable {self.ages} in return statement"

        # NameError: name 'cls' is not defined
        # return f"This is static method calling instance variable {cls.ages} in return statement"

        # NameError: name 'cls' is not defined
        # return f"This is static method calling class variable {cls.WHO} in return statement"
        return f"This is static method calling class variable {sex} in return statement"


father_obj = Father("Srinivasulu", 50)
print(father_obj.name)
print(father_obj.ages)
print(father_obj.behaviour)
print(father_obj.method_1())
print(father_obj.method_2())
print(father_obj.method_3())
print(father_obj.method_4("Male"))


class Son(Father):

    def __init__(self, name, age, behav):
        super().__init__(name, age)
        self.behav = behav

    def method_1(self):
        print(f"This is method1 calling name {self.name} in print statement")

    def method_5(self):
        return f"This is method5 calling behav {self.behav} in return statement"

    @classmethod
    def method_6(cls):
        # NameError: name 'self' is not defined
        # return f"This is class method calling instance variable age {self.ages} in return statement"

        # AttributeError: type object 'Father' has no attribute 'ages'
        # return f"This is class method calling instance variable age {cls.ages} in return statement"

        return f"This is method6 calling class variable {cls.WHO} in return statement"

    @staticmethod
    def method_7(sex):
        # NameError: name 'self' is not defined
        # return f"This is static method calling instance variable {self.ages} in return statement"

        # NameError: name 'cls' is not defined
        # return f"This is static method calling instance variable {cls.ages} in return statement"

        # NameError: name 'cls' is not defined
        # return f"This is static method calling class variable {cls.WHO} in return statement"
        return f"This is static method calling class variable {sex} in return statement"


son_obj = Son("Sumanth", 23, "Not bad")
