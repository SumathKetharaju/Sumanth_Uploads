# class Name
class State:

    # This is a class attribute or class variable
    HEAD = "Chief Minister"

    # Constructor -> In this we are define and assign attributes or parameters or variables
    def __init__(self, human, animal, bird):
        self.human = human
        self.animal = animal
        self.bird = bird
        self.ant = "red ants"
        self.insect = "xylophagous"

        print("Whenever an object is created, statement in __init__ is printed first")

    # Instance Method
    def human_do(self):
        print("Human can do anything if he desired")
        print(f"{self.human} is singing")
        return f"{self.human} is dancing"

    # Instance Method
    def animal_do(self):
        print("Animal lives in forest and eats lot of food")
        print(f"{self.animal} kills small animals and humans")
        return f"{self.animal} is running very fast"

    # Instance Method
    def bird_do(self):
        print("Bird lives in Trees branch")
        print(f"{self.bird} is singing")
        return f"{self.bird} is dancing"

    # Static method
    @staticmethod
    def district():
        print("Our district is Nellore")

    # class method
    @classmethod
    def village(cls):
        print("Our village is Buchireddypalem")


# calling the class variable or class attribute using class name
print(State.HEAD)
print()

# Here we are creating the fist object
AndhraPradesh = State("Mahesh", "Tiger", "Parrot")

# calling the class variable or class attribute using first object
print(AndhraPradesh.HEAD)
print()
# calling the instance variables or instance attributes using first object
print(AndhraPradesh.human)
print(AndhraPradesh.ant)
print()

# Type1 -> Here we are calling the Instance Methods using first object
State.human_do(AndhraPradesh)
State.animal_do(AndhraPradesh)
State.bird_do(AndhraPradesh)
print()

# Type2 -> Here we are calling the instance methods using first object
AndhraPradesh.human_do()
AndhraPradesh.animal_do()
AndhraPradesh.bird_do()
print()

# Type2 -> Here we are printing the instance methods using first object
print(AndhraPradesh.human_do())
print(AndhraPradesh.animal_do())
print(AndhraPradesh.bird_do())
print()

# Here we are creating the second object
Telangana = State("Sumanth", "Lion", "Peacock")

# calling the class variable or class attribute using second object
print(Telangana.HEAD)
print()
# calling the instance variables or instance attributes using second object
print(Telangana.animal)
print(Telangana.insect)
print()

# Type1 -> Here we are calling the Instance Methods using second object
State.human_do(Telangana)
State.animal_do(Telangana)
State.bird_do(Telangana)
print()

# Type2 -> here we are calling the instance methods using second object
Telangana.human_do()
Telangana.animal_do()
Telangana.bird_do()
print()

# Type2 -> here we are printing the instance methods using second object
print(Telangana.human_do())
print(Telangana.animal_do())
print(Telangana.bird_do())
print()

# Here we can changing the attribute's name
AndhraPradesh.human = "sunil"
print(AndhraPradesh.human_do())
print()

Telangana.animal = "Horse"
print(Telangana.animal_do())
print()

# here we are calling staticmethod
State.district()

# here we are calling classmethod
State.village()
