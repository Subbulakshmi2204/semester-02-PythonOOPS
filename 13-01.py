n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
non_zero_index=0
for i in range(len(l)):
    if l[i]!=0:
        l[non_zero_index],l[i]=l[i],l[non_zero_index]
        non_zero_index+=1
print("Updated array:",l)


n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
zero_index=0
for i in range(len(l)):
    if l[i]==0:
        l[zero_index],l[i]=l[i],l[zero_index]
        zero_index+=1
print("Updated array:",l)


n=int(input())
prices=[]
for i in range(n):
    prices.append(int(input()))
max_profit=0
for  i in range(1,len(prices)):
    if prices[i]>prices[i-1]:
        max_profit=prices[i]+prices[i-1]
print("Maximum profit:",max_profit)
