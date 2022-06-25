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
        print(f"The Total amount after depositing {dep_amount} to initial amount {self.opening_balance} "
               f"is --> {total_amount_after_deposit}")

    def with_draw(self, with_draw_amount):
        global total_amount_after_with_draw
        total_amount_after_with_draw = self.opening_balance - with_draw_amount
        print(f"The Total amount after with drawing {with_draw_amount} from initial amount {self.opening_balance} "
               f"is --> {total_amount_after_with_draw}")

    def get_balance(self):
        if self.type_of_account == "savings":
            return "deposit", total_amount_after_deposit
        else:
            return total_amount_after_with_draw

    def __repr__(self):
        if self.type_of_account == "current":
            return "This is Current account"
        elif self.type_of_account == "savings":
            return "This is savings account"
        else:
            return "This is for investment from account"


account_1 = Account("123", "John", 10.5, "current")
account_2 = Account("345", "John", 23.55, "savings")
account_3 = Account("123", "John", 12.45, "investment")

print(account_1)
print(account_2)
print(account_3)

account_1.deposit(23.45)
account_2.with_draw(12.33)
print(f"balance is --> {account_1.get_balance()}")
print(f"balance is --> {account_2.get_balance()}")

