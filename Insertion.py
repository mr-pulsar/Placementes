def insertion_Sort(a):
    for i in range(0,len(a)):
        b=i
        while b>0 and a[b]<a[b-1]:
            a[b],a[b-1]=a[b-1],a[b]
            b-=1
    return a
a=[1,3,2,4,5,3,2,4,78,7]
print(insertion_Sort(a))