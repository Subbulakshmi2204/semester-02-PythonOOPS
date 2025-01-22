
n=int(input("Enter the number of elements in array:"))
arr=[]
for i in range(n-1):#since there are n-1 elements in the array
    arr.append(int(input("Enter the elements:")))
tot_sum=0
for i in range(1,n+1):
    tot_sum+=i
arr_sum=sum(arr)
missing_no=tot_sum-arr_sum
print("The missing number is:",missing_no)

n=int(input("Enter the number of elements in array:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the elements:")))
lst=[]
for i in arr:
    if arr.count(i)==1:
        lst.append(i)
if lst:
    print("The numbers that appeared once are:",lst)
else:
    print("No numbers appeared only once")


n=int(input("Enter the number of elements in array:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the elements:")))
sorted_arr=sorted(arr)
print(sorted_arr)
if arr==sorted_arr:
    print("True")
else:
    print("False")


n=int(input("Enter the number of elements in the array:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the elements:")))
majority=None
max_count=0
for i in arr:
    occ=arr.count(i)
    if occ>n//2:
        majority=i
        break
if majority is not None:
    print("The majority element is:", majority)
else:
    print("No majority element found.")


def check_balanced_array(arr):
 total_sum = sum(arr)
 left_sum = 0
 equ=True
 for num in arr:
 if left_sum == total_sum - left_sum - num:
 equ=True
 return equ
 left_sum += num
arr = [1, 2, 3, 4, 10, 1, 2, 3]
print(check_balanced_array(arr))

n=int(input("Enter the number of elements in the array:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the elements:")))
target = int(input("Enter the target sum: "))
pairs=[]
for i in range(len(arr)-1):#5
 for j in range(i+1,len(arr)):#1,6
 if arr[i]+arr[j]==target:#0,1#0,2#0,3#0,4#0,5
 pairs.append((arr[i],arr[j]))
print(pairs)
