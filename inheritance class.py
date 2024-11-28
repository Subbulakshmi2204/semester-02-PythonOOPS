class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the name:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\n Name=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the salary:"))
    def displayInfo(self):
        self.displayEmployeeInfo()
        print("salary=",self.sal)
p=Perks()
p.getDetails()
p.displayInfo()
        
"""
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter ID")
        self.name=input("Enter the name")
        self.salary=int(input("Enter the salary"))
    def displayEmployeeInfo(self):
        print(f"ID={self.id}\n Name={self.name} \nSalary={self.salary}")
    def getSalary(self):
        return self.salary
class Perks(Employee):
    def calculateSalary(self):
        self.getEmployeeInfo()
        sal=self.getSalary()
        self.hra=sal*15/100
        self.da=sal*14/100
        self.total=self.hra+self.da
    def displayPerks(self):
        self.displayEmployeeInfo()
        print("Perks=",self.getSalary()+self.total)
p=Perks()
p.calculateSalary()
p.displayPerks()"""
        
