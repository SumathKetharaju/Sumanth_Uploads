class Father:

    NAME = "Srinivasulu"

    def __init__(self):
        self.shop = "Balaji vastralayam"
        self.house = "sennaiah house"
        self.phone = "Nokia"

    def sales(self):
        print(f"In shop {Father.NAME} sales clothes to the customers")

    def lives(self):
        print(f"{Father.NAME} lives in his house")

    def calls(self):
        print(f"{Father.NAME} uses phone to call his owner for bussiness purpose")


class Children(Father):

    CHID_NAME = "Sumanth"

    def __init__(self, degree, phone, laptop):
        super().__init__()
        self.degree = degree
        self.phone = phone
        self.laptop = laptop

    def job(self):
        print(f"{Children.CHID_NAME} completed his {self.degree} and doing a job")

    def calls(self):
        print(f"{Children.CHID_NAME} uses his phone to call his friends")

    def practice(self):
        print(f"{Children.CHID_NAME} uses his laptop to practice python programs")


father = Father()
print(father.shop)
# print(father.degree)
print(father.phone)
# print(father.laptop)
print(father.house)
print()

father.sales()
father.lives()
father.calls()
# father.job()
# father.practice()
print()


son = Children("Btech", "Vivo", "Dell")
print(son.degree)
print(son.phone)
print(son.laptop)
print(son.shop)
print(son.house)
print(son.phone)
print()

son.sales()
son.lives()
son.calls()
son.job()
son.practice()
