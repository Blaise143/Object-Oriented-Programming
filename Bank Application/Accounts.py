class Accounts:
    def __init__(self, name, account_number, balance, SSN):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.ssn = SSN

    def deposit(self, amount):
        balance += amount

    def show_info(self):
        print("Name :", self.name, "balance :", self.balance, "Account Number :", self.account_number)

    def transfer(self, amount: int, recepient):
        self.balance = self.balance - amount
        recepient.deposit(self.amount)

    def withdraw(self, amount):
        print("Old Balance : ", self.balance)
        print("Withdrawing ", self.amount)
        self.balance = self.balance -  amount
        print("Your new balance is ", self.balance)
