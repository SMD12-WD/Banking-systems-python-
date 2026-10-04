class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful, your new balance is R{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful, your new balance is R{self.balance}")

        else:
            print('''Insufficient funds
please check your balance''')

account1 = BankAccount("SMD", 10000)
account1.withdraw(12000)
#use of inheritance example below
class Check(BankAccount):
    pass
account2 = Check("SMD", 10000)
account2.deposit(1600)









