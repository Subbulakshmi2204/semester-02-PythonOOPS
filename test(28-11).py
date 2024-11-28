class Inventory:
    def __init__(self,proId,proName,proCount):
        self.proId=proId
        self.proName=proName
        self.proCount=proCount
    def display(self):
        print("Product ID:",self.proId)
        print("Product Name:",self.proName)
        print("Product Count:",self.proCount)
class Info(Inventory):
    def PrintDetails(self):
        self.display()
a=Inventory("A123","Soap",4)
a.display()


class Inventory:
    def __init__(self,proId,proName,proCount):
        self.proId=proId
        self.proName=proName
        self.proCount=proCount
    def display(self):
        print("Product ID:",self.proId)
        print("Product Name:",self.proName)
        print("Product Count:",self.proCount)
pro=Inventory("A123","Soap",4)
pro.display()
