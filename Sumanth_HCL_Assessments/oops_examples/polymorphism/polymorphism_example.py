"""
Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle).
However we could use the same method to color any shape. This concept is called Polymorphism.
"""


class Person1:

    def name(self):
        print(f"My name is Sumanth")

    def degree(self):
        print(f"I have completed my degree in 2019")


class Person2:

    def name(self):
        print(f"My name is Ravindra")

    def degree(self):
        print(f"I have completed my degree in 2018")


print("---------------------------------------first person details-------------------------------------------")
person_1 = Person1()
person_1.name()
person_1.degree()

print("---------------------------------------Second person details-------------------------------------------")
person_2 = Person2()
person_2.name()
person_2.degree()

print("---------------------------------------for calling same methods -------------------------------------------")


def person(man):
    man.name()
    man.degree()


person(person_1)
print("----------------------------")
person(person_2)
