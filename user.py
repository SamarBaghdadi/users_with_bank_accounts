from tkinter import N
from tkinter.font import names
from unicodedata import name

from bankAccount import bankAccount


class user:
    def __init__(self,name,email,account_name=[]):
        self.name=name
        self.email=email
        self.accounts=[]

        if len(account_name)==0:
            self.accounts.append(bankAccount(name,2))
        else:
            for i in range(len(account_name)):
                self.accounts.append(bankAccount(account_name[i],int_rate=2,balance=0))

    def make_depost(self,account_name,amount):
        account_id=self.fetch_id(account_name)
        print("the id of the name",account_name,"is index",account_id)
        self.accounts[account_id].deposit(amount)
        return self
    def fetch_id(self,name):
        id=-1
        for i in range (len(self.accounts)):
            print("account in position",i, "is ", self.accounts[i].account_name,"name is", name)
            if self.accounts[i].account_name==name:
                id=i
        return id

    def make_withdrawal(self,account_name,amount):
        account_id=self.fetch_id(account_name)
        self.accounts[account_id].withdraw(amount)
        return self

    def display_user_balance(self):
        for i in range (len(self.accounts)):
            print("User:",self.name,"account name :",self.accounts[i].account_name,"Balance:",self.accounts[i].balance)
        return self

    # def transfer_money(self,other_user,amount):
    #     self.account.withdraw(amount)
    #     other_user.account.deposit(amount)
    #     return self

michael=user("Machael","michael@michael.com",["first","second","third"])
rim=user("Rim","rim@rim.com")
# anis=user("Anis","anis@anis.com")
michael.make_depost("second",120)
michael.make_depost("third",584)
michael.make_depost("first",1)

michael.make_withdrawal("first",800)
michael.display_user_balance()
rim.make_withdrawal("Rim",400)
rim.display_user_balance()



# anis.make_depost(580).make_withdrawal(400).make_withdrawal(400).make_withdrawal(125).make_withdrawal(614).display_user_balance()

# michael.transfer_money(anis,458).display_user_balance()
# anis.display_user_balance()


    
