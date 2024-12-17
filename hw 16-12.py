
class User:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
    def set_username(self):
        self.__username=username
    def set_password(self):
        self.__password=password
    def checkpassword(self):
        digit=False
        char=False
        if len(self.__password)<8:
            return False
        if any(i.isdigit() for i in self.__password):
            digit=True
        if any(not i.isalnum() for i in self.__password):
            char=True
        if digit and char:
            print("The password is valid")
            return True
        else:
            if not digit or not char:
                return False
username=input("Enter the username:")
password=input("Enter the password:")
us=User(username,password)
if us.checkpassword():
    print(f"Username:{us.get_username()}\nPassword:{us.get_password()}")
else:
    print("Invalid credentials")

class Product:
    def __init__(self,name,price,stock):
        self.__name=name
        self.__price=price
        self.__stock=stock
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_stock(self):
        return self.__stock
    def set_name(self):
        self.__name=name
    def set_price(self):
        self.__price=price
    def set_stock(self):
        self.__stock=stock
    def check_price_and_stock(self):
        price=False
        stock=False
        if self.__price>0:
            price=True
        if type(self.__stock)==int and self.__stock>0:
            stock=True
        if price and stock:
            print("Valid Details")
            return True
        else:
            return False
name=input("Enter the name:")
price=int(input("Enter the price:"))
stock=int(input("Enter the stock available:"))
pro=Product(name,price,stock)
if pro.check_price_and_stock():
    print(f"Name:{pro.get_name()}\nPrice:{pro.get_price()}\nStock:{pro.get_stock()}")
else:
    print("No valid details")

class Student:
    def __init__(self,name,age,marks):
        self.__name=name
        self.__age=age
        self.__marks=marks
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_marks(self):
        return self.__marks
    def check_info(self):
        if not self.__age>5 and self.__age<100:
            raise ValueError("Age is invalid")
        if not self.__marks>0 and self.__marks<=100:
            raise ValueError("Marks are invalid")
try:
    name=input("Enter the name:")
    age=int(input("Enter the age:"))
    marks=int(input("Enter the marks:"))
    stu=Student(name,age,marks)
    stu.check_info()
    print(f"Name:{stu.get_name()}")
    print(f"Age:{stu.get_age()}")
    print(f"Marks:{stu.get_marks()}")
except ValueError as ve:
    print(ve)
        
            
