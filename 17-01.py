
def reverse(s):
    if len(s)<=1:
        return s
    else:
        return reverse(s[1:])+s[0]
user=input("Enter the string:")
reverse=reverse(user)
print("Reversed String:",reverse)

def cal_power(x,y):
    if y==0:
        return 1
    else:
        return x*cal_power(x,y-1)
a=int(input())
n=int(input())
result=cal_power(a,n)
print(f"The power of {a} to {n} is {result}")

n=int(input())
arr=[]
for i in range(n):
    l=list(map(int,input().split()))
    arr.append(l)
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
print("Transpose matrix is:")
for j in range(n):
    for i in range(n):
        print(arr[i][j],end=" ")
    print()

def is_palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return is_palindrome(s[1:-1])
string=input()
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

n=int(input())
arr=[]
for i in range(n):
    l=list(map(int,input().split()))
    arr.append(l)
tot=0
for row in arr:
    for colm in row:
        tot+=colm
print("The sum of all elements in the 2D array is",tot)

def sum_digit(n):
    if n<10:
        return n
    else:
        return n%10+sum_digit(n//10)
num=int(input())
result=sum_digit(num)
print(f"The sum of the digits of {num} is {result}")
