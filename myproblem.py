a="sankumarsansanjay"
b="san"
while (b in a):
    c=a.find(b)
    a=a[0:c]+a[c+len(b):]
    print(a)