
import random
class Customer:
    def __init__(self,cust_id,name,phno):
        self.cust_id=cust_id
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
class TicketBooking:
    def __init__(self):
        self.events={"Concert":{"Price":1000,"Seats":100},"Movie":{"Price":150,"Seats":200},"Drama":{"Price":100,"Seats":100}}
        self.booked_tickets=[] 
    def view_events():
        for events,details in self.events.items():
            print(f"{events}:{details['Price']} per ticket {details['Seats']}seats are available")
    def book_tickets(self,event_name,quantity,customer):
        if event_name in self.events:
            event=self.events[event_name]
            if event['Seats']>=quantity:
                totalprice=event['Price']*quantity
                event['Seats']-=quantity
                self.booked_tickets.append({"Customer_id":Customer.cust_id,"Event":event_name,"Quantity":quantity,"Total Price":totalprice,})
            else:
                print("Seats are not available!!!!")
        else:
            print("Event name is not available!!!!!!")
    def view_tickets(self,Customer):
        print("*******Ticket Information*******")
        cust_ticket=[t for t in self.booked_tickets if t["Customer_id"]==Customer.cust_id]
        if not cust_ticket:
            print("No tickets booked")
        else:
            for tick in cus_ticket:
                print(f"Event:{tick['event']},Quantity:{tick['quantity']},Total Cost:{tick['totalprice']}")
if __name__=="__main__":


    book=TicketBooking()            
    print("*******Welcome to TICKET Booking application*******")
    cust_id=input("Enter the customer id:")
    if Customer.verify_customer_id(cust_id):
        name=input("Enter your name:")
        phno=int(input("Enter your phone number"))
        customer=Customer(cust_id,name,phno)
        print("Valid!!!View the booking details")
    else:
        print("Invalid!!!Please register")
        name=input("Enter your name:")
        phno=int(input("Enter your phone number"))
        cust_id=Customer.gen_rand_id()
        customer=Customer(cust_id,name,phno)
        print("Your customer id is",cust_id)
    while True:
        print("*****Booking Info*****")
        print("\n1.View Events")
        print("\n2.Book tickets")
        print("\n3.View my tickets")
        print("\n4.Exit")
        choice=int(input("Enter any option to continue booking:"))
        if choice==1:
            book.view_events()
        elif choice==2:
            event_name=input("Enter the name of the event:")
            quantity=int(input("Enter the number of tickets:"))
            book.book_tickets(event_name,quantity,customer)
        elif choice==3:
            book.view_tickets(customer)
        


"""
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
"""
