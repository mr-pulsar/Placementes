'''Robin Karp Algorithm'''

a="sanjaydharunsanjayyadav"
b='san'
c=0
for i in range(len(a)-len(b)+1):
    if a[i:len(b)+i]==b:
        c+=1
print(c)
        

