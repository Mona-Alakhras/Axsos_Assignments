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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "primary": BankAccount(in_rate=0.02, balance=0),
            "savings": BankAccount(in_rate=0.05, balance=0)
        }

    def make_deposit(self, amount, account_type="primary"):
        self.account[account_type].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_type="primary"):
        self.account[account_type].withdraw(amount)
        return self

    def display_user_balance(self, account_type="primary"):
        print(f"User: {self.name}, Balance: {self.account[account_type].balance}")
        return self
    #bouns
    def transfer_money(self, other_user, amount,from_account_type="primary", to_account_type="primary"):
        self.account[from_account_type].withdraw(amount)
        other_user.account[to_account_type].deposit(amount)
        return self