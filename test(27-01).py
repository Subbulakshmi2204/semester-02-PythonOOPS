import re
def validation(name,department,password,re_password):
    while True:
        for i in name:
            if i.isalpha()==False:
                raise ValueError("USername must contain only alphabets")
            else:
                print("Enter your name:",name)
        ex= r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$%&#])[A-Za-z\d@$%&#]{1,8}$'
        if re.match(ex,password):
            print("Enter your password:",password)
        else:
            raise ValueError("Password length must be less than 8 and it must have 1 digit and 1 special character")
        if password!=re_password:
            raise ValueError("P
            
try:
    name=input()
    department=input()
    password=input()
    re_password=input()
    valid=validation(name,department,password,re_password)
except ValueError as e:
    print(e)
