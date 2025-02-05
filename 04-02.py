"""
#to convert a string into lower case without built-in function
ch=input()
for i in ch:
    if 'A'<=i<='Z':
        p=ord(i)
        q=chr(p+32)
    print(q,end='')
 
#to convert a string into upper case without built-in function
ch=input()
for i in ch:
    if 'a'<=i<='z':
        p=ord(i)
        q=chr(p-32)
    print(q,end='')
"""
def lowercase(ch):
    p=ord(ch)
    q=chr(p+32)
    print(q,end='')
def uppercase(ch):
    x=ord(ch)
    y=chr(x-32)
    print(y,end='')
str1=input()
for i in str1:
    if 'A'<=i<='Z':
        lowercase(i)
    elif 'a'<=i<='z':
        uppercase(i)
