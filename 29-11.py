class Employee:
    def __init__(self,name,Id,position):
        self.name=name
        self.Id=Id
        self.position=position
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nId:{self.Id}\nPosition:{self.position}")
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayaddressInfo(self):
        print(f"Street Name:{self.street}\nState:{self.state}\nCountry:{self.country}")
class EmployeeDetails(Employee,Address):
    def __init__(self,name,Id,position,street,state,country):
        super().__init__(name,Id,position)#super is used to get the variables of the immediate parent class
        Address.__init__(self,street,state,country)
    def displayEmp(self):
        self.displayEmployeeInfo()
        self.displayaddressInfo()
ed=EmployeeDetails("Subbu",100,"Manager","Shenoy Nagar","TamilNadu","India")
ed.displayEmp()
        
        
