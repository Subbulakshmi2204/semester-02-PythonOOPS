#multi-level inheritance
"""
class Employee:
    def __init__(self,name,emp_id,age):
        self.name=name
        self.emp_id=emp_id
        self.age=age
    def displayEmpInfo(self):
        print(f"Name of the employee:{self.name}\nEmployee Id:{self.emp_id}\nAge:{self.age}")
class HR(Employee):
    def __init__(self,name,emp_id,age,role):
        super().__init__(name,emp_id,age)
        self.role=role
    def displayHRInfo(self):
        self.displayEmpInfo()
        print(f"Role of the employee:{self.role}")
class Manager(HR):
    def __init__(self,name,emp_id,age,role,salary,hike):
        super().__init__(name,emp_id,age,role)
        self.salary=salary
        self.hike=hike
    def displayManagerInfo(self):
        self.displayHRInfo()
        print("Salary:",self.salary,"\nHike:",self.hike)
name=input()
emp_id=input()
age=int(input())
role=input()
salary=int(input())
hike=input()
man=Manager(name,emp_id,age,role,salary,hike)
man.displayManagerInfo()"""

#hybrid inheritance
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nAge:{self.age}")
class Manager(Employee):
    def __init__(self,name,age,eid):
        super().__init__(name,age)
        self.eid=eid
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print("Id:",self.eid)
class Developer(Employee):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def displayDeveloperInfo(self):
        self.displayEmployeeInfo()
        print("Department:",self.dept)
class TeamLeader(Manager,Developer):
    def __init__(self,name,age,eid,dept,teamsize):
        Employee.__init__(self,name,age)
        self.eid=eid
        self.dept=dept
        self.teamsize=teamsize
    def displayTeamInfo(self):
        print("Team size:",self.teamsize)
name=input()
age=int(input())
eid=input()
dept=input()
Ts=int(input())
tl=TeamLeader(name,age,eid,dept,Ts)
tl.displayManagerInfo()
tl.displayDeveloperInfo()
tl.displayTeamInfo()

