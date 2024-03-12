input="aaaabbcccn"
c=''
for i in input:
    if i not in c:
        c+=i
for i in c:
    v=input.count(i)
    print("".join((f'{v}',i)),end="")
