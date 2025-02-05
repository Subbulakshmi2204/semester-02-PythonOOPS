arr=list(map(int,input("Enter the elements of the array separated by space:").split()))
print("Original Array:",arr)
even=[]
odd=[]
for i,j in enumerate(arr):
    if i%2==0:
        even.append(i)
        print(f"Index{i},Value:{j}")
    else:
        odd.append(i)
        print(f"Index{i},Value:{j}")
print("Elements at Odd position:")
for i,j in enumerate(odd):
    print(f"Index{i},Value:{j}")
print("Elements at Even position:")
for i,j in enumerate(even):
    print(f"Index{i},Value:{j}")
