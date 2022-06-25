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


father = Father("Srinivasulu", 50, "Male", "Good")
# print(father)  # <__main__.Father object at 0x0000025427386D60>  --> If we don't use __repr__ it will print address
print(father)  # This is a Father class, If we use __repr__ in our class it prints whatever we write in that function

print("--------------------------------------------methods calling using object--------------------------------------")
print(father.hobbies())
print(father.work())


print("-----------------------------------------Attributes calling using object-------------------------------------")
print(father.name)
print(father.age)
print(father.gender)
print(father.behaviour)
print(father.WHO)

print("------------------------------------------methods calling using class name-----------------------------------")
# print(Father.hobbies())
# print(Father.work())


print("-----------------------------------------Attributes calling using class name----------------------------------")
print(Father.WHO)
# print(Father.name)
# print(Father.age)
# print(Father.gender)
