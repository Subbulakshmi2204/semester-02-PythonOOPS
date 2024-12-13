class Student:
    def __init__(self):
        self.stu_id=input("Enter the Id:")
        self.name=input("Enter the Name:")
        self.grade=input("Enter the Grade:")
    def validate_id(self):
        id_len=len(self.stu_id)
        if id_len==7:
            if self.stu_id[0:3]=="STU":
                if self.stu_id[3:7].isdigit()==True:
                    print("Valid")
                else:
                    print("Last 4 cases are not valid")
            else:
                print("First 4 cases are not valid")
        else:
            print("Length is not valid")
    def validate_name(self):
        if len(self.name)>=2 and all(char.isalpha() or char.isspace() for char in self.name):
            print("Valid name")
        else:
            print("Not Valid")
    def validate_grade(self):
        if self.grade[0].isdigit==False:
            print("Invalid")
        number=int(self.grade.split('')[0])
        if number<1 and number>12:
            print("Invalid")
        else:
            print("Valid")
    def display(self):
        print(self.stu_id)
        print(self.name)
        print(f"{self.grade}TH")
s=Student()
s.validate_id()
s.validate_name()
s.validate_grade()
s.display()
