"""
n=5
start=1
for i in range(1, n + 1):
    row=[]
    for j in range(i):
        row.append(start)
        start+=1
    print(" ".join(map(str, row)))


arr=list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
candidate=None
count=0
for num in arr:
    if count==0:
        candidate=num
    count+=(1 if num==candidate else -1)
count=arr.count(candidate)
if count>len(arr)//2:
    print("The majority element is:", candidate)
else:
    print("No majority element")


class Student:
    def __init__(self,name,roll_no,subjects_marks):
        self.name=name
        self.roll_no=roll_no
        self.subjects_marks=subjects_marks
    def average_marks(self):
        total_marks=sum(self.subjects_marks.values())
        num_subjects=len(self.subjects_marks)
        return total_marks/num_subjects if num_subjects>0 else 0
students = [
    Student("Alice", 101, {"Math": 80, "Science": 75, "English": 85}),
    Student("Bob", 102, {"Math": 78, "Science": 88, "English": 82}),
    Student("Charlie", 103, {"Math": 95, "Science": 92, "English": 90}),
    Student("David", 104, {"Math": 70, "Science": 80, "English": 77}),]
topper = max(students, key=lambda student: student.average_marks())
print(f"Topper: {topper.name}, Roll No: {topper.roll_no}, Average Marks: {topper.average_marks():.2f}")
"""
def product_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    if "discount" in kwargs:
        price=kwargs.get("price")
        discount=kwargs.get("discount")
        final_price=price-(price*discount/100)
        print(f"Final price after discount: {final_price:.2f}")
    else:
        print("No discount available")
product_info(name="Laptop", brand="Dell", price=80000, discount=10)
