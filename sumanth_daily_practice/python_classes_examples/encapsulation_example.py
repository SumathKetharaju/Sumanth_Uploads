class Parent:

    def __init__(self):
        self._a = 1


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("It is called parent class")
        print(self._a)


child = Child()
parent = Parent()
print(child._a)
