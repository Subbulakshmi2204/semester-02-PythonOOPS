"""
#lambda arguments :expression
add=lambda  a,b:a+b
print(add(1,2))
"""
L1=list(map(int,input().split()))
square=map(lambda x:x**2,L1)
print(list(square))
"""
#filter even numbers in a list
L2=list(map(int,input().split()))
even=filter(lambda x:x%2==0,L2)
print(list(even))

t=[(1,2),(6,3),(4,1)]
t1=sorted(t,key=lambda x:x[0])
print(t1)


Name=['subbu','vicky','hasly']
Salary=[20000,40000,10000]
ph_no=[982835213,8056206373,78455095]
S=zip(Name,Salary,ph_no)
sort=sorted(S,key=lambda k:k[1])
print(sort)
"""
