def selection(arr):
    for i in range(0,len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr
a=[1,2,4,5,6,2,3,5,78,8]
print(selection(a))