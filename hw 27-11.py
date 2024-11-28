
class Student:
    def __init__(self,name,rollno,dep,sub1,sub2,sub3):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.per=((sub1+sub2+sub3)/3)*100
    def grade(self):
        if self.per>=80:
            print("Grade A")
        elif self.per>=60:
            print("Grade B")
        elif self.per>=40:
            print("Grade C")
        else:
            print("Invalid Input")
s=Student("Subbulakshmi",55,"AI",97,89,82)
s.grade()


class Student:
    def __init__(self,name,age,course,grade):
        self.name=name
        self.age=age
        self.course=course
        self.grade=grade
    def show(self):
        print(f"student Details-Student Name {self.name},Student Age {self.age},Student Course {self.course},Student Grade {self.grade}")
    def __del__(self):
        print("ALL DETAILS ARE DELETED")
stu1=Student("Subbu",18,"AI","A")
stu1.show()
del stu1
