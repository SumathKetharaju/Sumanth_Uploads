total_amount_after_deposit = 0
total_amount_after_with_draw = 0


class Account:

    def __init__(self, account_number, account_holder, opening_balance, type_of_account):
        self.account_number = account_number
        self.account_holder = account_holder
        self.opening_balance = opening_balance
        self.type_of_account = type_of_account

    def deposit(self, dep_amount):
        global total_amount_after_deposit
        total_amount_after_deposit = dep_amount + self.opening_balance

    def with_draw(self, with_draw_amount):
        global total_amount_after_with_draw
        total_amount_after_with_draw = self.opening_balance - with_draw_amount

    def get_balance(self):
        if self.type_of_account == "current":
            self.opening_balance = total_amount_after_deposit
            return self.opening_balance
        elif self.type_of_account == "savings":
            return total_amount_after_with_draw
        else:
            return total_amount_after_deposit

    def __repr__(self):
        if self.type_of_account == "current":
            return f"Account[{self.account_number}] - {self.account_holder}, current account = {self.opening_balance}"
        elif self.type_of_account == "savings":
            return f"Account[{self.account_number}] - {self.account_holder}, savings account = {self.opening_balance}"
        else:
            return f"Account[{self.account_number}] - {self.account_holder}, investment account = {self.opening_balance}"


account_1 = Account("123", "John", 10.05, "current")
account_2 = Account("345", "John", 23.55, "savings")
account_3 = Account("567", "Phoebe", 12.45, "investment")
print(account_1)
print(account_2)
print(account_3)
account_1.deposit(23.45)
account_2.with_draw(12.33)
print(f"balance is on account1 is--> {account_1.get_balance()}")
print(f"balance is on account2 is --> {account_2.get_balance()}")



