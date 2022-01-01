# calling the method from object
class Computer:

# for intialize the variables we use __init__ method

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):

        print("config is",self.cpu, self.ram)


com1 = Computer('i5',16)
com2 = Computer('ryzen',8)

com1.config()
com2.config()


