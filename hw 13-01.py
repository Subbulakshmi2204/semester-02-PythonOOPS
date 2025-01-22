
g =int(input())
gas=[]
for i in range(g):
    gas.append(int(input()))
c=int(input())
cost=[]
for i in range(c):
    cost.append(int(input()))
total_gas=0 
total_cost=0 
current_gas=0 
starting_station=0 
for i in range(len(gas)):
    total_gas+=gas[i]
    total_cost+=cost[i]
    current_gas+=gas[i]-cost[i]
    if current_gas<0:
        starting_station=i+1
        current_gas=0 
if total_gas>=total_cost:
    print(f"Starting gas station index:{starting_station}") 
else:
    print("Not possible to complete the circuit")

r=int(input())
ratings=[]
for i in range(r):
    ratings.append(int(input()))
n=len(ratings) 
candies=[1]*n 
for i in range(1,n):
    if ratings[i]>ratings[i-1]:
        candies[i]=candies[i-1]+1 
for i in range(n-2,-1,-1):
    if ratings[i]>ratings[i+1]:
        candies[i]=max(candies[i],candies[i+1]+1) 
result=sum(candies) 
print(result)
