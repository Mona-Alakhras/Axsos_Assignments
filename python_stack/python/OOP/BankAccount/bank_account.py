class BankAccount:
    def __init__(self, in_rate, balance=0):
        self.in_rate = in_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self    

    def display_account_info(self):
        print(f"Balance: {self.balance}")  
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.in_rate    
        return self    


account1 = BankAccount(0.02, 100)
account2 = BankAccount(0.05, 500)

account1.deposit(50).deposit(100).deposit(150).withdraw(20).yield_interest().display_account_info()
account2.deposit(200).deposit(500).withdraw(20).withdraw(40).withdraw(60).withdraw(10).yield_interest().display_account_info()