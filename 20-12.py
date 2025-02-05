def roman_to_int(num):
    roman=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result=0
    for v,i in roman:
        while num.startswith(i):
            result+=v
            num=num.removeprefix(i)#removeprefix will remove the first value been found
    print(result)
roman_to_int('CXX')

"""
sym=input("Enter a symbol:")
roman_symbols=[('M',1000),('CM',900),('D',500),('CD',400),('XC',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',5),('I',1)]
num_result=0
for i,j in roman_symbols:
    while sym.startswith(i):
        num_result+=j
        sym=sym[len(i)]
print(num_result)"""


import re
def verify_password(password):
    ex=r'^(?=.*[a-z])(?=.*[0-9]).{8,}$'
    if re.match(ex,password):
        print("Password is strong")
    else:
        print("Password is not strong")
password=input("Enter the password")
verify_password(password)

