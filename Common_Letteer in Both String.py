def Common_letter(a,b):
    f=''
    c=set(a)
    d=set(b)
    v=c.intersection(d)
    for i in v:
        f+=i
    return sorted(f)

a="sanjay"
b="dharun"
print(*Common_letter(a,b))