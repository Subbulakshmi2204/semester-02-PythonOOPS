
class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Amount Deposited: {amount}")
        else:
            print("Amount to deposit should be positive")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds...")
        elif amount<0:
            print("Withdraw amount should be positive")
        else:
            self.balance-=amount
            print(f"Amount Withdraw: {amount}")
    def check_balance(self):
        print(f"Balance: {self.balance}")
my_acc=BankAccount()
my_acc.deposit(10000)
my_acc.withdraw(1700)
my_acc.check_balance()

class Cosmetic:
    def __init__(self,p_name="Foundation",p_brand="Nybae",p_price=150,p_category="makeup"):
        self.p_name=p_name
        self.p_brand=p_brand
        self.p_price=p_price
        self.p_category=p_category
    def display(self):
        print(f"Name={self.p_name}\nBrand={self.p_brand}\nPrice={self.p_price}\nCategory={self.p_category}")
cos=Cosmetic()#default constructor-non parameterised arguments
cos.display()
        
