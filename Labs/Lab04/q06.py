class BankAccount:

    def __init__(self, number, balance, date, name):
        self.number = number
        self.balance = balance
        self.date = date
        self.name = name

    def deposit(self, money, number):
        if number == self.number:
            self.balance += money
            print(f"New Balance is {self.balance}")
            return
        print("Authorization Unsuccessful")
        return

    def withdraw(self, money, number):
        if (number) == (self.number) and self.balance >= money:
            self.balance -= money
            print(f"New Balance is {self.balance}")
            return
        print("Authorization Unsuccessful or balance not enough")
        return

    def check_balance(self, number):
        if number == self.number:
            print(f"Balance is {self.balance}")
            return
        print("Authorization Unsuccessful")
        return


Account = BankAccount("123", 10000, "09/sep/24", "Ali")
Account.deposit(200, "123",)
Account.withdraw(20000, "123")
Account.withdraw(1000, "123")
Account.check_balance("123")