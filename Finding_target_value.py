nums=list(map(int,input("Enter the number:").split()))
target=int(input("Enter the Target Value:"))
c=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            c.append(i)
            c.append(j)
print(c)