#ENCAPSULATION
"""
class Student:
    _id=123#Since double underscore is been mentioned it is a private variable and we will get the result as attribute error
    def __init__(self,name):
        self._name=name
    def display(self):
        print("Name:",self._name)
s=Student("Ria")
s.display()
print(s._id)


class Student:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def display(self):
        print(f"Name:{self._name}\nAge:{self._age}")
name=input()
age=int(input())
s=Student(name,age)
s.display()"""

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def displayEmployeeInfo(self):
        print(f"Employee Name:{self.name}\nSalary:{self.__salary}")
class TL(Employee):
    def __init__(self,name,salary,role,teamsize):
        super().__init__(name,salary)
        self.role=role
        self.teamsize=teamsize
    def displayTLInfo(self):
        self.displayEmployeeInfo()
        print(f"Role:{self.role}\nTeamsize:{self.teamsize}")
name=input()
salary=int(input())
role=input()
teamsize=int(input())
emp=TL(name,salary,role,teamsize)
print('Name:',emp.name)
print('Salary:',emp._Employee__salary)#name mangling
print('Role:',emp.role)
print('Teamsize:',emp.teamsize)
