n=int(input())
n1=0
n2=1
count=0
if n<=0:
    print("Enter a positive integer")
elif n==1:
    print(n1)
else:
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
        
