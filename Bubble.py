def bubble(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i], a[j] = a[j], a[i]
    return a

a=[3,2,1,6,5,4]
print(*bubble(a))