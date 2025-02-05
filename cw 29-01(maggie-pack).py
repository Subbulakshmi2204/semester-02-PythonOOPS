class Maggie_Pack:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def check_budget(self,budget):
        if not isinstance(budget,(int,float))or budget<0:
            raise ValueError("Budget cannot be negative!!!!!")
        return True
    def calculate_balance(self,budget):
        return budget-self.price
    def suggest_packs(self,budget):
        try:
            self.check_budget(budget)
            if budget>self.price:
                print(f"You can buy {self.name} pack")
                print(f"Your remaining balance is {self.calculate_balance(budget)}")
            elif budget==self.price:
                print(f"You can buy {self.name}. No balance is remaining")
            else:
                print(f"You will not be able to afford {self.name} pack.")
        except ValueError as ve:
            print(ve)
small=Maggie_Pack("small",20)
regular=Maggie_Pack("regular",30)
big=Maggie_Pack("big",50)
packets=[small,regular,big]
try:
    budget=float(input('Enter the budget:'))
    for pack in packets:
        pack.suggest_packs(budget)  
except ValueError:
    print("Enter a numerical value")
