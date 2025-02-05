class Pizza_Size:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def check_budget(self,budget):
        if not isinstance(budget,(int,float)) or budget<0:
            raise ValueError("Budget cannot be negative!!!!")
        return True
    def calculate_price(self,budget):
        return budget-self.price
    def validate_price(self,price):
        try:
            self.check_budget(budget)
            if budget>self.price:
                print(f"You can buy {self.name} pizza")
                print(f"The balance is {self.calculate_price(budget)}")
            elif budget==self.price:
                print(f"You can buy {self.name} pizza")
                print("There isn't any balance!!")
            else:
                print(f"You cannot afford {self.name} pizza")
        except ValueError as ve:
            print(ve)
small=Pizza_Size('Small',70)
medium=Pizza_Size('medium',120)
large=Pizza_Size('large',200)
size=[small,medium,large]
try:
    budget=float(input("Enter your budget:"))
    for i in size:
        i.validate_price(budget)
except ValueError as ve:
    print(ve)
    
