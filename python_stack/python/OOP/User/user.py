class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_blance = 0

    def make_deposit(self, amount):
        self.account_blance += amount   

    def make_withdrawal(self, amount):
        self.account_blance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_blance}")

    #bouns
    def transfer_money(self, other_user, amount):
        self.account_blance -= amount
        other_user.account_blance += amount

mona = User("mona" , "mona@gmaol.com")
sondos = User("sondos" , "sondos@gmaol.com")
aya = User("aya" , "aya@gmaol.com")

mona.make_deposit(50)
mona.make_deposit(100)
mona.make_deposit(150)
mona.make_withdrawal(50)
mona.display_user_balance()

sondos.make_deposit(200)
sondos.make_deposit(300)
sondos.make_withdrawal(50)
sondos.make_withdrawal(50)
sondos.display_user_balance()

aya.make_deposit(500)
aya.make_withdrawal(50)
aya.make_withdrawal(100)
aya.make_withdrawal(20)
aya.display_user_balance()


mona.transfer_money(aya,100)
mona.display_user_balance()
aya.display_user_balance()





