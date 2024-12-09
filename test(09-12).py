
class Student:
    def __init__(self,name,rollno,mark1,mark2,mark3):
        self.name=name
        self.rollno=rollno
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def displayStudentInfo(self):
        print(f"Name of the student:{self.name}\nRoll No:{self.rollno},\nMark-1:{self.mark1},\nMark-2:{self.mark2},\nMark-3:{self.mark3}")
class Markmanagement(Student):
    def __init__(self,name,rollno,mark1,mark2,mark3,total,percentage):
        super().__init__(name,rollno,mark1,mark2,mark3)
        self.total=total
        self.percentage=percentage
    def displayMarkInfo(self):
        self.displayStudentInfo()
        print(f"Total Marks:{self.total},\nPercentage:{self.percentage}")
mark1=int(input())
mark2=int(input())
mark3=int(input())
total=mark1+mark2+mark3
percentage=(total/300)*100
stu=Markmanagement("Subu",55,mark1,mark2,mark3,total,percentage)
stu.displayMarkInfo()
