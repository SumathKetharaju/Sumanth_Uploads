class Computer:

# config method

    def config(self):

        print("i5, 16gb, 1tb")


com1 = Computer()

com2 = Computer()

# one way to call function
Computer.config(com1)
Computer.config(com2)
# another way to call function most of the cases we use this
com1.config()
com2.config()