
"""
import re
def check_pangram(string):
    ex=r'[*a-z]{26}$'
    if re.match(ex,string):
        print("The string is pangram")
    else:
        print("The string is not a pangram")
string=input("Enter the string:")
val=check_pangram(string)

"""
class Student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def displayInfo(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if not self.name.isalpha():
            raise ValueError("Name must be in characters")
    def calculate_grade(self):
        tot=mark1+mark2+mark3
        per=(tot/300)*100
        if not (0 <= self.mark1 <= 100) or not (0 <= self.mark2 <= 100) or not (0 <= self.mark3 <= 100):
            raise ValueError("Marks must be between 0 and 100")
        elif per>=90:
            print("Grade A")
        elif per>=80:
            print("Grade B")
        elif per>=65:
                print("Grade C")
        else:
            print("Grade D")
try:
    name=input("Enter the students name:")
    mark1=int(input())
    mark2=int(input())
    mark3=int(input())
    stu=Student(name,mark1,mark2,mark3)
    stu.displayInfo()
    stu.calculate_grade()
except ValueError as e:
    print(e)       
