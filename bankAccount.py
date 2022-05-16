class bankAccount:
    def __init__(self,account_name,int_rate,balance=0):
        self.account_name=account_name
        self.balance=balance
        self.interest_rate=int_rate/100

    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        self.balance-=amount
        return self
    def display_account_info(self):
        print("Balance: $",self.balance)
        return self
#     def yield_interest(self):
#         if self.balance>=0:
#             self.balance+=self.balance*self.interest_rate
#         else:
#             print("the balance",self.balance,"is negative, no yielding is possible")
#         return self

# michael_account=bankAccount(5,200)
# michael_account.deposit(420).deposit(100).deposit(985).withdraw(542).display_account_info()

# anna_account=bankAccount(10)
# anna_account.deposit(10).deposit(234).withdraw(54).withdraw(201).withdraw(14).withdraw(301).yield_interest().display_account_info()

