class Superclass:

    print("This is superclass")

    def method_1(self):
        print("This is method1 in Super class")

    def method_2(self):
        print("This is method2 in Super class")


class Subclass:

    print("This is subclass")

    def method_1(self):
        print("This is method1 in Sub class")

    def method_2(self):
        print("This is method2 in Sub class")


def common_method(method):
    print("This is common_method")
    method.method_1()


superclass = Superclass()
subclass = Subclass()

common_method(superclass)
common_method(subclass)
