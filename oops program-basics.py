"""
class Student:
    s_name="Subbu"
    s_dept="AI"
s=Student()
print(f"Name={s.s_name}\nDepartment={s.s_dept}")

class Student:
    s_name=' '
    s_dept=' '
s1=Student()
s2=Student()
s1.s_name="Subbu"
s1.s_dept="AI"
s2.s_name="Hasly"
s2.s_dept="AI"
print(f"Name={s1.s_name}\nDepartment={s1.s_dept}")
print("\nAssign values based on object2")

class Student:
    name="Subbu"
    dept="AI"
    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}")
s=Student()
s.display()

class Student:
    ID=''
    def __init__(self,name=''):
        self.name=name
    def getData(self):
        self.ID=input("Enter the ID")
    def display(self):
        print("Student detail")
        print("Name=",self.name)
        print("ID=",self.ID)
s_name=input("Enter the name")
s=Student(s_name)
s.getData()
s.display()

class library:
    def __init__(self):
        self.bname="Pride and prejudice"
        self.bauthor="Jane"
    def display(self):
        print(f"Book name={self.bname}\nBook author={self.bauthor}")
lib=library()
lib.display()

class Student:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}")
stu=Student("Subbu","AI")
stu.display()

class Student:
    def __init__(self,dept,age=18,name='subbu'):
        self.age=age
        self.name=name
        self.dept=dept
    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}\nage={self.age}")
stu=Student("AI")
stu.display()"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name={self.name}\nAge={self.age}")
class Student(Person):
    def __init__(self,name,age,stu_id,stu_dept):
        super().__init__(name,age)
        self.stu_dept=stu_dept
        self.stu_id=stu_id
    def printDetails(self):
        self.display()
        print(f"ID={self.stu_id}\nDepartment={self.stu_dept}")
s=Student('Subbu',18,55,'AI')
s.printDetails()

        
