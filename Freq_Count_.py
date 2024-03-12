a=list(map(int,input("Enter the Numbers:").split()))
v=int(input("Enter the Count:"))
b=a
c=[]
dict={}
for i in b:
    dict[i]=a.count(i)
for i,j in dict.items():
    if j == j>=v:
        c.append(i)
print(c)