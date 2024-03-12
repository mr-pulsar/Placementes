a=[[1,2,4],
   [5,6,7],
   [9,10,11]]
c=[]
while a:
    c+=a.pop(0)
    if a and a[0]:
        for i in a:
            c.append(i.pop())
    if a:
        c+=(a.pop()[::-1])
print(c)

