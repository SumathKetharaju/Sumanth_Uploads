class Father:

    FATHER = "father"

    def __init__(self):
        self.name = "Subbarao"
        self.house = "Apartment"
        self.mobile = "Vivo"

    def who_is_this(self):
        print(f"I am {self.name}")

    def where_are_you(self):
        print(f"I am in {self.house}")

    def call(self):
        print(f"I am using my {self.mobile} mobile to call")


class Son(Father):

    SON = "son"

    def __init__(self, branch, address, number):
        super().__init__()
        self.branch = branch
        self.address = address
        self.number = number

    def who_are_you(self):
        print(f"I am a {self.branch} engineer")

    def where_are_you(self):
        print(f"I am in {self.address}")

    def what_are_you_doing(self):
        print(f"I am studying {self.branch} engineering")


father = Father()
father.who_is_this()
print(father.house)
son = Son("civil", "Buchireddypalem", 369)
son.where_are_you()
print(son.number)

