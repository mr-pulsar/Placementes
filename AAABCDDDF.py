a="AAABCDDDF"
for i in range(0,len(a),3):
    c=[]
    b=i
    for i in range(3):
        if a[b] not in c:
            c.append(a[b])
        b+=1
    print(c)