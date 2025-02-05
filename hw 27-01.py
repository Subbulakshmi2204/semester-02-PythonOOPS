"""
n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the elements:")))
print("Original array:",arr)
to_remove = int(input("Enter the element to remove: "))
if to_remove in arr:
    arr.remove(to_remove)
else:
    print(f"{to_remove} is not in the array.")

print("New array:",arr)


n = int(input("Enter the number of elements in the array: "))
arr = [input(f"Enter element {_+1}: ").strip() for _ in range(n)]
# Non-Inverse Order
print("Your Non-Inverse Order Array is:", arr)
# Inverse Order
inverse_arr = list(reversed(arr))
print("Your Inverse Order Array is:", inverse_arr)
"""


import re
def get_name():
    while True:
        name = input("Enter your Name: ").strip()
        if not name.isalpha():
            print("Error: Name should only contain alphabets. Please try again.")
        else:
            return name
def get_department():
    department = input("Enter your Department: ").strip()
    return department
def get_password():
    while True:
        password = input("Enter your Password: ").strip()
        re_password = input("Re-Type your Password: ").strip()
        
        if len(password) > 8:
            print("Error: Password should not exceed 8 characters. Please try again.")
            continue
        if not any(char.isdigit() for char in password):
            print("Error: Password must contain at least one number. Please try again.")
            continue
        if not any(char in '@#$%^&*!' for char in password):
            print("Error: Password must contain at least one special character. Please try again.")
            continue
        if password != re_password:
            print("Error: Passwords do not match. Please try again.")
            continue
        return password
def display_details(name, department, password):
    print(f"Your Encoded Name is: {'X'*len(name)} - Fresher")
    print(f"Your Department is: {'X'*len(department)}")
    print(f"Your Password is: {'X' * len(password)}")
    print(f"Re-Type your Password: {'X' * len(password)}")
# Main Execution
def main():
    name = get_name()
    department = get_department()
    password = get_password()
    display_details(name, department, password)
main()
