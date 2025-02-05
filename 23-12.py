
#returns sum of the digit
n=int(input())
count=0
while n!=0:
    rem=n%10
    count+=rem
    n//=10
print(count)

#counts the number of words
string=input("Enter a string:")
lst=string.strip()
count=len(lst)
print(count)

#common elements between two list
n1=int(input("Enter the number of elements in list1:"))
n2=int(input("Enter the number of elements in list2:"))
list1=[]
list2=[]
for i in range(n1):
    list1.append(int(input("Enter the elements:")))
for i in range(n2):
    list2.append(int(input("Enter the elements:")))
print(list1)
print(list2)
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)

#extract phone numbers from text
text=input("Enter the text:")
phone=[]
for i in text:
    if i.isdigit()==True:
        phone.append(i)
for i in phone:
    print(i,end='')

#extract hashtags from text
import re
text=input("Enter the text:")
ex=r'#\w+'
result=re.findall(ex,text)
print(result)

#sort list of integers
n=int(input("Enter the number of elements in the array:"))
elements=list(map(int,input().split()))
for i in range(n):
    for j in range(0,n-i-1):
        if elements[j]>elements[j+1]:
            elements[j],elements[j+1]=elements[j+1],elements[j]
print(elements)

#1
id=True
Login="LIB1234"
for i in range(5):
    login=input("Enter the login id:")
    if login==Login:
        id=True
        print("Login id is valid")
        break
    else:
        id=False
        print("Your id is wrong")
        print(f"you have {5-(i+1)} attempts")
if not id:
    print("Login id is invalid")

#2
n=int(input("Enter the number of elements in the list"))
list1=[]
for i in range(n):
    elements=int(input("Enter the elements"))
    list1.append(elements)
print(list1)
list1=set(list1)
print("The list without duplicates:",list1)
list1=list(list1)
list1.sort(reverse=True)
print("The list in descending order:",list1)

#valid email address
import re
email=input("Enter the email id:")
ex=ex=r'^[a-z0-9._%+-]+@gmail\.com$'
if re.match(ex,email):
    print("Valid")
else:
    print("Not a valid")

#7 bank account
print("1.Deposit \n2.Withdraw \n3.View Balance \n4.Exit")
balance=10000
while True:
    choice=int(input("Enter the choice:"))
if choice==1:
    print("Deposit")
    deposit=int(input("Enter the amount to be deposited:"))
    balance+=deposit
    print(f"You have successfully deposited {deposit}!!!")
elif choice==2:
    print("Withdraw")
    withdraw=int(input("Enter the amount to be withdrawed:"))
    if balance>=withdraw:
        print("fYou have successfully withdrawed {withdraw}!!!")
        balance-=withdraw
    else:
        print("You have insufficient balance.....")
elif choice==3:
    print("Check balance")
    print(balance)
else:
    exit()
        


        
