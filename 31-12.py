
"""
class Bonus_pool:
    def __init__(self,n):
        self.n=n
    def fact(self,n):
        if n==0 or n==1:
            return 1
        else:
            return n*self.fact(n-1)
    def sum_fact(self):
        lst=[]
        lst=[self.fact(i) for i in range(1,self.n+1)]
        return sum(lst),lst
num=int(input("Enter the number of employees:"))
bn=Bonus_pool(num)
sum_fact,lst=bn.sum_fact()
print("Factorials:",", ".join([f"{i + 1}!= {lst[i]}" for i in range(len(lst))]))
print("Sum of all factorials:",sum_fact)
"""

def fibonacci(n):
    n1=0
    n2=1
    print(n1)
    print(n2)
    for i in range(n+1):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)
        if n3>n:
            print(f"First Fibonacci number greater than {n}:{n3}")
            break
n=int(input("Enter the threshold:"))
fibonacci(n)

#3
sentence=input("Enter a sentence:")
n1=sentence.split()
n=[]
for i in n1:
    n.append(len(i))
    s=sorted(n)
print(s)
a=s[-1]
for i in n1:
    if len(i)==a:
        print(f"Longest word:'{i}' with length {a}")
        
    
