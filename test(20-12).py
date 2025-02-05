import re
def verify_password(password):
    ex=r'^(?=.*1[a-z])(?!\D)(?!["@#$%^&*"])(?=.*3[A-Z]).{12}$'
    if re.match(ex,password):
        print("Password is strong")
    else:
        print("Password is not strong")
password=input("Enter the password:")
verify_password(password)
