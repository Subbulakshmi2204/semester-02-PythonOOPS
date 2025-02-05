
roman=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
n=int(input("Enter the number to convert:"))
ans=''
for val,letter in roman:
    while n>=val:
        ans+=letter
        n-=val
print("The roman value for the given integer is:",ans)
        

ro=input("Enter the roman value:")
roman={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}

result=0
prev_value=0
for char in reversed(roman):
    current_value=roman[char]
    if current_value<prev_value:
        result-=current_value
    else:
        result += current_value
print(f"The integer value of {roman} is {integer_value}")
