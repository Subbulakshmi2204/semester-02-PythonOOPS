"""
import random
class Customer:
    def __init__(self,cust_id,name,phno):
        self.cust_id=cusst_id
        self.name=name
        self.phno=phno
    def gen_rand_id(self):
        c_id=random.randint(1000,9999)
        return f"TICK{c_id}"
    def verify_customer_id(cust_id):
        length=len(cust_id)
        no=0
        ucase=0
        for i in cust_id:
            if i.isdigit():
                no+=1
            else:
                ucase+=1
            if length>=8 and no>=4 and cust_id[0:4]=="TICK":
                print("Valid Customer_Id")
            else:
                print("Invalid Customer_Id")
print("*******Welcome to TICKET Booking application*******")
cust_id=input("Enter the customer id:")"""

class Password:
    def validate(text):
        length=len(text)
        no=0
        ucase=0
        for i in text:
            if i.isdigit():
                no+=1
            else:
                ucase+=1
        if length>=8 and no>=4 and text[0:4]=="TICK":
            print("Valid Customer_Id")
        else:
            print("Invalid Customer_Id")
txt=input("Enter a Customer Id:")
Password.validate(txt)
