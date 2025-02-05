
str1=input()
str2=input()
merged=[]
i=0
j=0
while i<len(str1) and j<len(str2):
    merged.append(str1[i])
    merged.append(str2[j])
    i+=1
    j+=1
merged.append(str1[i:])
merged.append(str2[j:])
result=''.join(merged)
print(result)


bed=list(map(int,input().split()))
n=int(input())
count=0
for i in range(len(bed)):
    if bed[i]==0:
        left=(i==0 or bed[i-1]==0)
        right=(i==len(bed)-1 or bed[i+1]==0)
        if left and right:
            bed[i]=1
            count+=1
            if count>=n:
                print(True)
                break
            else:
                print(False)
