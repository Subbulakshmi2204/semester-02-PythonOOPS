class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPersonInfo(self):
        print("Name:",self.name,"\nAge:",self.age)
class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def displayEmployeeInfo(self):
        print("Employee Id:",self.Id)
class Manager(Person):
    def __init__(self,name,age,Id,salary):
        super().__init__(name,age)
        self.salary=salary
    def displayManagerInfo(self):
        print("\nSalary:",self.salary)
class Job(Employee,Manager):
    def __init__(self,name,age,Id,salary,phoneno):
        Manager.__init__(self,name,age,Id,salary)
        self.phoneno=phoneno
    def displayJobInfo(self):
        print("\nPhone Number:",self.phoneno)
job=Job("Subbu",18,55,75000,9382835213)
job.displayPersonInfo()
job.displayJobInfo()
job.displayManagerInfo()
job.displayEmployeeInfo()


