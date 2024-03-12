#PRIME OR NOT
'''n=int(input("Enter:"))
if n<2:
    print("Not A Prime")
elif n==2:
    print("Prime")
else:
    for i in range(22,int(n**5)+1):
        if n%i==0: 
            print("Not a Prime")
        else:
            print("Prime")'''

#FIBBO
'''n=int(input("Enter:"))
a=0
b=1
c=0
for i in range(n):
    print(c,end=" ")
    c=a+b
    b=a
    a=c'''
'''current_year=int(input("Current Year"))
birth_year=int(input("Birth Year"))
age=current_year-birth_year
print(age,end=" ")'''

'''a=float(input("Enter:"))
b=float(input("Enter:"))
sum=a+b
sub=a-b
print("SUM:",sum,end=" ")
print("Sub:",sub,end=" \n")'''

'''sanjay="vannakkam Tamilan"
print(sanjay.replace('v','s'))'''
'''sanjay="kumar"
print('kumr' in sanjay)
x=9+3*3
print(x)

x=9
y=9
z=x==y
print(z)

cel=float(input("Enter:"))
fahrenheit=(cel*9/5)+32
print("Fahrenheit:",fahrenheit,end=" ")
x=int(input("Enter the weight:"))
y=input("(k)g or L(bs)")
if y.upper()=="K":
    converted=x/0.45
    print("Converted:",converted)
else:
    converted=x*0.45
    print("Converted:",converted)
n=1
while n>=1:
    print(n)
    n+=1

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end=" ")
    print()

pos=-1
def Linear_earch(list,n):
    for i in range(0,n):
        if list[i] == n:
            globals()['pos']=i
            return True
    return False

list=[1,2,3,45,6,7,8]
n=45
if Linear_earch(list,n):
    print("found",pos)
else:
    print("Not Found")

arr=[1,2,36,4,3,32,42,2]
arr.sort()
print(arr)

listt=[]
n=int(input("Enter:"))
for i in range(0,n):
    el=int(input())
    listt.append(el)
    l=sorted(listt)
print(l)

def Linear_earch(list,n):
    i=0
    for i in range(0,n):
        if list[i]==n:
            return True
    return False

list=[3,4,521,42,23,213]
n=213
if Linear_earch (list,n):
    print("Found")
else:
    print("Nill")


list=[]
n=int(input("Enter:"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
    a=sorted(list)
print(a)

def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid
            

def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid
            
def snake(t):
    for i in range(0,len(t)):
        if (i%2):
            for j in t[i]:
                print(j,end=" ")
        else:
            for j in t[i][::-1]:
                print(j,end=" ")
a=[
    [1,2,3,4,5],
    [2,3,4,5,6],
    [7,6,3,3,2],
    [1,2,3,4,5],
]
snake(a)

lis=[]
n=int(input())
for i in range(n):
    ele=int(input())
    lis.append(ele)
    a=sorted(lis)
print(a)'


def snake(s):
    for i in range(0,len(s)):
        if (i%2==0):
            for j in s[i]:
                print(j,end=" ")
        
        else:
            for j in s[i][::-1]:
                print(j,end=" ")
n=[
    [1,2,3,4,4,5],
    [323,23232,32,54,2,2],
    [74,535,0,0,75,34,24],
]
snake(n)
def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

def snake(s):
    for i in range(0,len(s)):
        if (s%2):
            for j in s[i]:
                print(j,end=" ")
        else:
            for j in s[i][::-1]:
                print(j,end=" ")
s=[
    [1,2,3,45,21132],
    [1,2,3,4,5,6],
    [3443,224,4,24,3,2]
]
snake(s)


lis=[]
n=int(input("Enter the number of times:"))
for i in range(0,n):
    ele=int(input())
    lis.append(ele)
    a=sorted(lis)
print(a)

def snake(t):
    for i in range(0,len(t)):
        if (i%2): 
            for j in t[i]:
                print(j,end=" ")
        else:
            for j in t[i][::-1]:
                print(j,end=" ")
a=[
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    ]
print(snake(a))


def linear_c(list,n):
    i=0
    for i in range(0,n):
        if list[i]==n:
            return True
    return False
list=[2,32,1,3,2,34,33]
n=3
if linear_c(list,n):
    print("Found")
else:
    print("Not found")

pos=-1
def linear_c(list,n):
    i=0
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
    return False
list=[2,32,1,3,2,34,33]
n=3
if linear_c(list,n):
    print("Found",pos)
else:
    print("Not found")

dharun=[]
dharun.append(56)
dha=dharun.pop()
print(dha)
print(dharun)

def bubble(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j] = num[j+1]
                num[j+1]=temp
arr=[1,23,45,64,3,53,2]
bubble(arr)
print(arr)

def insertionsort(arr):
    print(arr)
    for i in range(1,len(arr)):
        b=i
        while b>0 and arr[b]<arr[b-1]:
            arr[b-1],arr[b]=arr[b],arr[b-1]
            b=-1
            print(arr)
arr=[0,4,6,9,15,12,11323]
insertionsort(arr)
print(arr)


def ins(san):
    for i in range(1,len(san)):
        b=i
        while b>0 and san[b]<san[b-1]:
            san[b],san[b-1]=san[b-1],san[b]
            b-=1
            print(san)




def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]> arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
arr=[43,21,33,67,3]
bubble(arr)
print(arr)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left= arr[:mid]
        right= arr[mid:]

        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)

#linear

def linear(list,n):
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False
list=[1,2,3,4,556,564]
n=6
if linear(list,n):
    print("Found")
else:
    print("Nil")

#FIBBO
n=int(input("Enter:"))
a=0
b=1
s=0
for i in range(n):
    print(s,end=" ")
    s=a+b
    b=a
    a=s

def bubble(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

list=[34,56,78,321,2]
bubble(list)
print(list)

def inseration_ii(list):
    for i in range(2,len(list)):
        b=i
        while b>0 and list[b]<list[b-1]:
            list[b],list[b-1]=list[b-1],list[b]
            b-=1
            print(list)
list=[4,5,3,2,1]
inseration_ii(list)
print(list)

def insertion(arr):
    for i in range(2,len(arr)):
        b=i
        while b>0 and arr[b]<arr[b-1]:
            arr[b],arr[b-1]=arr[b-1],arr[b]
            b-=1
            print(arr)
arr=[5,4,3,22,1]
insertion(arr)
print(arr)


def snake(t):
    for i in range(0,len(t)):
        if (i%2):
            for j in t[i]:
                print(j,end=" ")
        else:
            for j in t[i][::-1]:
                print(j,end=" ")
a=[
    [1,2,3,4,5],
    [5,43,3,21,1],
    [34,2,35,6,42],
    [32,67,5432,313],
]
print(snake(a))

def heapify(arr, n, i):
    largest = i  
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i) 
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)


def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,i)
def heap_sort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
arr=[23,232,23,1313,2]
heap_sort(arr)
print(arr)

def palindrome(s):
    return s== s[::-1]
s="SANJA"
if palindrome(s):
    print("PAli")
else:
    print("NP")


n=int(input("Enter:")) 
m=n**0.5
if (m//1)==m:
    print("Perfect")
else:
    print("NP")   

lis=[]
n=int(input("Enter:"))
for i in range(n):
    ele=(input("Enter:"))
    lis.append(ele)
    a=sorted(lis)
    print(a)

def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
arr=[6,5,8,64,5]
bubble(arr)
print(arr)

def bubble(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j] = num[j+1]
                num[j+1]=temp
arr=[1,23,45,64,3,53,2]
bubble(arr)
print(arr)

arr=[1,32,444,678654,67,65,493]
arr.sort(reverse=True)
print(arr)

n=(input("Enter:"))
sum=0
for i in n:
    sum += int(len(i))**3
if sum==int(len(n)):
    print("Amst")
else:
    print("NA")


def linear(arr,n):
    for i in range(n):
        if arr[i]==n:
            return True
    return False


arr=[1,2,3,7,8]
n=8
print(linear(arr,n))

n=input("Enter:")
sum=0
for i in n:
    sum+=int(len(i))**3
if sum==len(n):
    print("AMSTRONG")
else:
    print("NA")

def anagram(n1,n2):
    if (sorted(n1)==sorted(n2)):
        print("Anagram")
    else:
        print("NA")

n1=input("Enter")
n2=input("Enter")
a=anagram(n1,n2)
print(a)

n=input("Enter:")
sum=0
for i in n:
    sum+=int(i)**3
if sum==int(n):
    print("Amstrong")
else:
    print("NA")

n=input("Enter:")
sum=0
for i in n:
    sum+=int(i)**3
if sum==int(n):
    print("AMSTRONG")
else:
    print("NA")
def anagram(n,m):
    if (sorted(n)==sorted(m)):
        print("Anagram")
    else:
        print("NA")
n=input("Enter String1:")
m=input("Enter String2:")
print(anagram(n,m))


n=int(input("Enter:"))
m=3.14*(n**2)
print(m)
n=int(input("Enter:"))
m=n**0.5
if (m//1)==m:
    print("Perfect Square")
else:
    print("Not A Perfect Square")



def bubble(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
arr=[1,4,2,4,5,3,5]
bubble(arr)
print(arr)


n=int(input("Enter:"))
if n<2:
    print("Not a prime")
elif n==2:
    print("prime")
else:
    for i in  range(2,int(n**0.5)+1):
        if n%i==0:
            print("not a prime")
        else:
            print("prime")


n=(input("Enter:"))
sum=0
for i in n:
    sum+=int(i)**3
if sum==int((n)):
    print("Amstrong")
else:
    print("Na")

n=int(input("Enter:"))
if n<2:
    print("Not a Prime")
elif n==2:
    print("Prime")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Not A Prime")
        else:
            print("Prime")
n=int(input("Enter:"))
m=n**0.5
if (m//1)==m:
    print("Perfect")
else:
    print("NA")

n=(input("Enter:"))
sum=0
for i in n:
    sum+=int(i)**3
if sum==int(len(n)):
    print("Amstrong")
else:
    print("Na")


def spiral_order(matrix):
    ans = []
    while matrix:
        ans += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                ans.append(row.pop())
        if matrix:
            ans += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ans.append(row.pop(0))
    return ans

# Example usage
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
print(spiral_order(matrix))



nums=[2,7,11,15]
target=nums[0],nums[1]
print(nums[0]+nums[1])

x=int(input("enter:"))
if x>3:
    print(x, "is Greather than 3")
else:
    print("Sorry")

def spiral(matrix):
    result=[]
    while matrix:
        result+=matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result+=matrix.pop()[::-1]


        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

a=[[1,2,3],
   [3,2,1],
   [1,2,3],]

print(spiral(a))

def spiral_order(matrix):
    ans = []
    while matrix:
        ans += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                ans.append(row.pop())
        if matrix:
            ans += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ans.append(row.pop(0))
    return ans

# Example usage
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
print(spiral_order(matrix))

def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1]=temp
pr=[2,3,43,21,23]
bubble(pr)
print(pr)


def insertion(arr):
    for i in range(1,len(arr)):
        b=i
        while b>0 and arr[b]<arr[b-1]:
            arr[b],arr[b-1]=arr[b-1],arr[b]
            b-=1
            print(arr)
arr=[3,43,221,3233]
insertion(arr)
print(arr)

n=(input("Enter:"))
sum=0
for i in n:
    sum+=int(i)**3
if sum==int(len(n)):
    print("Am")
else:
    print("Nil") 


lis=[]
n=int(input("Enter:"))
for i in range(n):
    ele=int(input("Enter:"))
    lis.append(ele)
    a=sorted(lis)
print(a)


n=int(input("Factorial:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)



def sanke(t):
    for i in range(len(t)):
        if i%2:
            for j in t[i]:
                print(j,end=" ")
        else:
            for j in t[i][::-1]:
                print(j,end=" ")
t=[[1,2,3],
   [3,2,1],
   [5,7,6]]
print(sanke(t))

add=lambda a,b:a+b
print(add(453342,22414111114))

def spiral(matrix):
    ans=[]
    while matrix:
        ans+=matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                ans.append(row.pop())
        if matrix:
            ans+=matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ans.append(row.pop(0))
    return ans
ans=[[3,2,1],
     [8,6,5],
     [6,4,7]]
print(spiral(ans))
        
def spiral_order(matrix):
    ans = []
    while matrix:
        ans += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                ans.append(row.pop())
        if matrix:
            ans += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ans.append(row.pop(0))
    return ans

# Example usage
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
print(spiral_order(matrix))

Tamil=int(input())
English=int(input())
Maths=int(input())
Science=int(input())
Social=int(input())
a=(Tamil+English+Maths+Science+Social)/5
print(a)

def linear(arr,n):
    for i in range(0,len(arr)):
        if arr[i]==n:
            return True
    return False


arr=[3,4,5,6,7,8,9,10,11,12]
n=999
cc=linear(arr,n)
print(cc)


def anagram(n,m):
    if (sorted(n)==sorted(m)):
        return True
    return False
N=(input("Enter:"))
m=(input("Enter:"))
print(anagram(N,m))

n=int(input("Enter:"))
a=0
b=1
c=1
for i in range(1,n):
    c=a+b
    b=a
    a=c
    print(c,end=" ")

a=25
b=float(a)
print(b)

def san(a,b):
    ali=0
    bob=0
    for i,j in zip(a,b):
        if i>j:
            ali+=1
        elif i<j:
            bob+=1
    return ali,bob
a=[1,2,3]
b=[3,2,1]
c=san(a,b)
print(c)


def spiral(matrix):
    result=[]
    while matrix:
        result+=matrix.pop(0)[::-1]
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop(0))
        if matrix:
            result+=matrix.pop()

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
    return result

a=[[1,2,3],
   [4,5,6],
   [9,7,8]]
print(spiral(a))


a=[10,20,15,2,23,90,67]
san=[]
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        print(a[i])


def rotate(a):
    c=a[-1:]+a[:-1]
    print(c)
a=list(map(int,input().split()))
print(rotate(a))

num=[1,2,3,4,67,5,6,7,8,90]
rotates=int(input("Enter:"))
c=num[-rotates:]+num[:-rotates]
rotates=rotates % len(num)
print(c)


def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1] and arr[j+1]<arr[j]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
arr=[1,2,3,54,6,42,12,434]
bubble(arr)
print(arr)

list=[1,5,7,0]
k=6
count=0
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==k:
            count+=1
print(count)

a=[12,3,2,5,6,0]
for i in range(len(a)-1):
    count=0
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            count+=1
    print(count)

a=[10,15,2,5,6,10]
for i in range(1,len(a)-1):
    for j in range(i):
        if a[i-1]<a[i] and a[i]>a[i+1]:
            print(a[i])



def diagonalDifference(arr):
    temp = 0
    emp = 0
    for i in range(0,len(arr)):
        temp = temp + arr[i][i]
    
    for j in range(0,len(arr)):
        emp = emp + arr[j][len(arr)-1-j]
    
    return abs(temp - emp)



arr=[[1,2,3],z[4,5,6],[7,8,9]]
print(diagonalDifference(arr))


a=[1,1,0,-1,-1]
for i in range(0,len(a)):
    if a]:
        i%len(a)
    print(i)
a=[1,2,3,4,5]
sum=0
add=0
for i in range(0,len(a)+1):
    sum=sum+i
print(sum)
for j in range(0,len(a)):
    add=add+j
print(add) 


n=[1,2,3,4,5]
s=0
for i in n:
    s+=i
print(s)


s=[1,2,3,4,5]
for i in range(0,len(s)):
    a=s[-1:]+s[:-1]
print(a)

a=str(input())
captial=[]
for i in a.split():
    captial.append(i.capitalize())
cap=' '.join(captial)
print(cap)

def duplicate(arr):
    sum=[]
    for i in arr:
        if i not in sum:
            sum.append(i)
    return sum
arr=[1,2,3,4,1]
print(duplicate(arr))

a=[6,5,4,3,45,2,1]
sum=0
for i in range(len(a)-1):
    
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            sum+=1
    print(sum)


def diagonalDifference(arr):
    temp = 0
    emp = 0
    for i in range(0,len(arr)):
        temp += arr[i][i]
    
    for j in range(0,len(arr)):
        emp = emp + arr[j][len(arr)-1-j]
    
    return abs(temp - emp)



arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
print(diagonalDifference(arr))

list=[2,3,4,5,6,7,8,9]
l=[]
for i in range(len(list)):
    if list[i]%2==0:
        l.append(list[i])
for j in range(len(list)):
    if list[j]%2!=0:
        l.append(list[j])
print(l)

def Prime(n):
    if n<2:
        print('Not a Prime')
    elif n==2:
        print("prime")
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print("Not a Prime")
            else:
                print("Prime")
n=int(input("Enter:"))
print(Prime(n))



a=[1,3,4,5,7]
c=0
for i in a:
    if n<2:
        print('Not a Prime')
    elif n==2:
        print("prime")
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print("Not a Prime")
            else:
                print("Prime")
                c+=1    
print(c)

n=int(input())
for i in range(10,n+1):
    if n>9:
        d=i%10
        d1=i//10
        d2=d1-d
        if (d2==1 or d2==-1):
            print(i)

n=5
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

list=[1,4,4,5,3,28,4]
k=4
c=0
for i in range(len(list)):
    if list[i]==k:
        c+=1
    break    
print(c)

a=['watermelon','boy','girls','school','sanjay','leorty']
b=sorted(a)
c=b[::-1]
print(c[0:3])
print(c)

a=[4,5,6,4,1,4,8,5,4]
n=8
k=4
count=0
for i in range(len(a)):
    if a[i]==k:
        count+=1
    
    if a[i]==n:
        break
print(count)

a=20
for i in range(a):
    q=i%10
    w=i//10
    p=(q-w)
    if p==1 or p==-1:
        print(i,end='')

a=[1,3,4,32,42,4]
length=len(a)
mid=length//2
first=sorted(a[:mid])
second=sorted(a[mid:],reverse=True)
print(first+second)

def custom(arr):
    length=len(arr)
    for i in range(length//2):
        for j in range(length//2-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    for i in range(length//2,length-1):
        for j in range(length//2,length-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr
arr=[9,8,7,6,7,4,32,2]
print(custom(arr))

word_lst = list(map(str,input().split()))
N = int(input())
sorted_lst = sorted(word_lst, key=lambda x: len(x), reverse=True)
for i in range(N): 
   print(sorted_lst[i], end=" ")


a=[10,3,4,5,6,7,8,67]
b=[5,6,7,65]
if min(a)<=min(b) and max(a)>=max(b):
    print("True")
else:
    print('False')

def san(n):
    num=1
    while num >=1:
        yield num
        num+=1
    for i in san(10):
        print(i, end=" ")


a={0:'san',1:'qwerty',33:'opi'}
print(a|({1:'dharun'}))

a=[1,2,3,4,5]
n=int(input("Enter the Length of First Four:" ))
b=int(input("Enter the Length of Second Four:" ))
print(sum(a[n:]),sum(a[:b]))


def custom(arr):
    length=len(arr)
    for i in range(length//2):
        for j in range(length//2-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    for i in range(length//2,length-1):
        for j in range(length//2,length-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[9,8,7,6,7,4,32,2]
print(custom(arr))


class goa():
    name=''
    drink=''
    def beach():
        print("Let's Party.....")
    def ride():
        print("Ride")
sanjay=goa()
yadav=goa()

sanjay.name='Sanjay'
yadav.name='Yadav'

yadav.drink='yes'
sanjay.drink='no'
print(sanjay.name)
print(sanjay.drink)

a=[[2,3],[4,5]]
q=[p+t for p,t in a]
print(q)

def maxSubArraySum(self,arr,N):
    sum=0
    max=arr[0]
    for i in range(N):
        sum+=arr[i]
        if sum>max:
            max=sum
        if sum<0:
            sum=0
    return max


a=str(input("Enter"))
if a==a[::-1]:
    print('Palindrome')
else:
    print("Not a Palindrome")


b=str(input("Enter:"))
a=len(b)
h=int(a/2)
if b[:h]==b[h:]:
    print("Symmetic")
else:
    print("Not a Symmetic") 

a=["geeks for geeks"]
b=['g','e']
c=[]
d=str(a)
for i in range(len(b)):
    count=0
    for j in range(len(d)):
        if b[i]==d[j]:
            count+=1
    c.append(count)
for i in range(0,len(b)):
    print(b[i],":",c[i],end="")

a="qwerty poi asdfg"
r=a.split()[::-1]
print(' '.join(r))



a='sanjay dharun yadav'
n=['s','a']
d=dict()
for i in n:
    d[i]=a.count(i)
print(d)


a='sanjay dharun yadav'
b=a.replace('a','o')
print(b)

a='sanjay12345dharun'
for i in range(1):
    if a[i].isalnum():
        print(' True')
    else:
        print(' False')


arr=['orange','girl','boy','watermelon']
K = int(input())
a = sorted(arr, key=len, reverse=True)
b = a[:K]
print(b)'''


"sanjay the little"
'''b=a.split()
k=len(b)
print(k[0])

for i in range(0,len(a)):
    if i==0 or i==k:
        print(a[i].upper(),end="")
    else:
        print(a[i],end="")
x=a.split()
y= []
for i in x:
    if len(i) >1 :
        opt = i[0].upper() + i[1:-1].lower() + i[-1].upper()
        y.append(opt)
    else:
        opt = i.upper()
        y.append(opt)
v = " ".join(y)
print(v)

a="geeks for geeks "
b='Learning from Geeks for Geeks'
c=a.split()
d=b.split()
e=[]
for i in c:
    if i not in :
        e.append(i)
for i in d:
    if i not in e:
        e.append(i)
e=list(set(e))
print(e)

def UncommonWords(A, B):
    A=A.split()
    B=B.split()
    x=[]
    for i in A:
        if i not in B:
            x.append(i)
    for i in B:
        if i not in A:
            x.append(i)
    x=list(set(x))
    return x

Original="sanjay"
ap=''
for i in Original:
    if i not in ap:
        ap+=i
print(ap)

a='110111'
s=True
for i in a:
    if i not in ['0','1']:
        s=False
if s:print('True')
else:print('False')

a= 'Gfg is best for geeks and cs'
s1='is'
s2='and'
t1=a.find(s1[-1])
t2=a.find(s2)
print(t1)
print(a[t1+1:t2].strip())

a='ji'
b='ing'
d='ly'
c=len(a)
if c>=3 and b not in a:
    print(a+b)
elif c>=3 and b in a:
    print(a+d)
else:
    print(a)

a='10100'
s=True
for i in a:
    if i not in ['0','1']:
        s=False
if s:print("True")
else:print("False")

a=int(input("Enter:"))
o=list()
while a!=0:
    e=a%2
    o.append(e)
    a=a//2
o.reverse()
for i in o:
    print(i,end="")

a= 'Gfg is best for geeks and cs'
b='is'
c='and'
d=a.find(b[-1])
e=a.find(c)
print(a[d+1:e].strip())


def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

aq=[5,6,3,252,42,553]
bubble(aq)
print(aq)

n=(input("Enter:"))
sum=0
for i in n:
    sum+=int(i)**3
if sum==int(len(n)):
    print('Amst')
else:
    print("Na") 

def insertion(arr):
    for i in range(2,len(arr)):
        b=i
        if b>0 and arr[b]<arr[b-1]:
            b-=1
            return arr

a=input("Enter")
b=len(a)-2
if len(a)>2:
    print(a[b:]*4)
else:
    print('Sry')

a='010f10'
ab=True
for i in a:
    if i not in ['0','1']:
        ab=False
if ab:print("True")
else:print("False") 

a='anjay is a bafd and iop'
b='is'
c='and'
d=a.find(b[-1])
e=a.find(c)
print(a[d+1:e].strip())

import random
a=int(input("Enter:"))
b=random.random()
if a==b:
    print("Found and Matched")
else:
    print("Not Matched")

a = 'sanjay12s'
total_sum = 0
a_s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in a:
    if i in a_s:
        total_sum += int(i)
print(total_sum)


a='khokho789'
b=len(a)
c=int(b/2)
if a[c:]==a[:c]:
    print("Sym")
else:
    print("Not Sym")

a='sanja in khokho789'
aa=a.replace(' ','')
c=len(aa)
print(c)


a='sanjay'
b=''
for i in a:
    if i not in b:
        b+=i
print(b)


a='sanjay yadav dharun'
b='sanjay dharun'
c=a.split()
d=b.split()
e=[]
for i in c:
    if i not in d:
        e.append(i)
for i in d:
    if i not in c:
        e.append(i)
e=list(set(e))
print(e)


def linear(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return True
    return False    
arr=[1,2,38,9,7,543,21,190,10]
n=7
print(linear(arr,n))



a='sanjay is very important and '
b='is'
c='and'
d=a.find(b)
e=a.find(c)
print(a[d:e].strip())


a='sanjay123'
b=['0','1','2','3','4','5','6','7','8','9']
c=0
for i in a:
    if i in b:
        c+=int(i)
print(c)


a='sanjay dharun yadv'
b=a.split()
for i in b:
    if len(i)>1:
        san=i[0].upper()+i[1:-1].lower()+i[-1].upper()
        print(san,end=' ')
    if len(i)==1:
        print(i.upper(),end=' ')



a=input("Enter:")
b='AEIOUSaeious'
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(''.join(c))


a='Geeks'
for i in range(5,0,-1):
    print(a[0:i],end=' ')
a=[5, 7, 2, 7, 5, 2, 5]
c=0
for i in range(len(a)):
    if a[i]%2!=0:
        c+=1
    else:
        a[i]==1
        print
print(c)


n=17
finger=['Thumb','Ring','Middle','index','Small']
result=n%8
if result<5:
    print(finger[n-1])
if result>5:
    print(finger[10-result-1])

#Sum of Natural Numbers

def sum(a):
    return a*(a+1)//2
a=5
print(sum(a))


def nth(a,n,d):
    return a+(n-1)*d
a=4
n=4
d=5
print(nth(a,n,d))

def sum_of(a,n,d):
    return (n / 2) * (2 * a + (n - 1) * d)
a=3
d=4
c=5
asa=sum_of(a,n,d)
print(asa)

a=['1','2','3','4','5']
b=['1','2','3','4','5']
c=zip(a,b)
print(list(c))

a=['SAnjya',23]
firsstname,age=a
print(a)

import random
Alphabet='qwertyuioplkjhgfsadzxcvbnm'
Number='1234567890'
symbol='!@#$%^&*()_+=-[]\|'
length=16
password=Alphabet+Number+symbol
aa=''.join(random.sample(password,length))
print(aa)


import random
Name1=input("Enter Your Name(Player1):")
Name2=input("Enter Your Name(Player2):")
player1=input(f"{Name1.title()} Enter Your Choice:")
player2=input(f"{Name2.title()} Enter Your Choice:")
length=1
a=''.join(random.sample(player1,length))
print(f'{Name1.upper()} choice is:',player1)
b=''.join(random.sample(player2,length))
print(f'{Name2.upper()} choice is:',player2)

if player1==player2:print("Match tied")
elif player1>player2:print(f"{Name1.title()} Wins")
elif player1 == 'Pencil' and player2 == 'Paper':print(f"{Name1.title()} Wins")
elif player1 == 'Paper' and player2 == 'Pencil':print(f"{Name2.title()} Wins")
elif player1 == 'Paper' and player2 == 'Scissores':print(f"{Name2.title()} Wins")
elif player1 == 'Scissores' and player2 == 'Paper':print(f"{Name1.title()} Wins")
else:print(f"{Name2.title()} Wins")


a= [56,5,71,4,5,4,5,5]
ab=a.count(a)
print(ab)

a=int(input("Enter the Value:"))
l=[]
while a!=0:
    r=a%2
    l.append(r)
    a=a//2
l.reverse()
for ele in l:
    print(ele,end='')


a={1:"Sanjay",2:"F",3:"Kumar"}
for i in a:
    b=a.fromkeys(a,"Sanjay")
print(b)

a='-123'
print(eval(a))

a=[1,2,3,4,2,3,4,5]
for i in a:
    if a.count(i)==1:
        print(i,end=" ")

import random
if random.randint(0,1)==1:
    print("Head")
else:
    print("Tail")

list=['Sanjay','dhaarn','yadav']
a={i:len(i) for i in list}
print(a)

name=input("Enter:")
if name:
    print(name)
else:
    print("N/A")


name1=input("Enter:")
name=name1 or 'Srry User doesnot exist'
print(name)

a="sanjay faang"
b='s','a'
c=dict()
for i in b:
    c[i]=(a.count(i))
    print(c)

a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            b=[]
            if i!=j and j!=k and k!=i :
                b.append(i)
                b.append(j)
                b.append(k)
                print(b)

for i in range(3):
    for j in range(3):
        for f in range(3):
            print(i,j,f)
        print()

a= [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]
d=[]
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            if a[i]==b[j]==c[k]:
                d.append(a[i])
                d.append(b[j])
                d.append(c[k])
e=list(d)
print(*e)

a=100
for i in range(1,a+1):
    if i!=34 and i!=88:
        print(i,end=" ")

for i in range(2,3):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

def diagonalDifference(a):
    s=0
    d=0
    for i in range(len(a)):
        s+=a[i][i]
    for j in range(len(a)):
        d+=a[j][len(a)-1-j]
    return (s-d)
a=[[1,2,3],
   [9,8,7],
   [6,9,8]]
print(diagonalDifference(a))

a=[4,5,6,7,8,9,10]
a[0],a[1]=a[1],a[0]
a[2],a[3]=a[3],a[2]
a[4],a[5]=a[5],a[4]
print(a)
def swap(a):

    for i in range(0,len(a)):
        for j in range(i+1):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
        return a
        
a=[4,5,6,7,8,9,10]
print(swap(a))


a=[1,2,5,5,5]
b=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            b.append(a[i])
print(b,end="")


a = 'ASsasewW'
b = 'AaEeIiOoUuSs'

for char in a:
    if char in b:
        print(char.swapcase(), end='')
    else:
        print(char, end='')

a='ProSoccer'
b=a[::-1]
print(b[:-1]+b[-1:].lower(),end=" ")



a = [1, 2, 3, 4, 5]
b = []
target = 7
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            b.append(a[i])
            b.append(a[j])
print(b)

a='asasafghkK'
b='AaeEiIoOuU'
for i in a:
    if i in b:
        print(i.swapcase(),end='')
    else:
        print(i,end='')

def linear_search(arr,n):
    for i in range(0,len(arr)+1):
        if arr[i]==n:
            return True
    return False
aee=[1,2,34,56]
n=34
print(linear_search(aee,n))

a=[2,7,9,5,4,0]
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[j]>a[j+1]:
            temp=a[j+1]
            a[j+1]=a[j]
            a[j]=temp
print(a)

pos=[]
def linear_search(arr,n):
    for i in range(0,len(arr)+1):
        if arr[i]==n:
            globals['pos']
            return True
    return False
aee=[1,2,34,56]
n=34
print(linear_search(aee,n)

A = {1,2,5,4,0}
B = {2,4,5,0,1}
c=[]
for i in A:
    if A==B :
        c.append(i)
print(c)


nums = [2,7,11,15]
c=[]
for i in range(0,len(nums),2):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==9:
            c.append(i)
            c.append(j)
print(c)

def is_valid_tag(tag):
    if len(tag) != 9:
        return "Invalid"
    digits = tag[:2] + tag[3:6] + tag[7:9]
    letter = tag[2]
    for i in range(0, 8,2):
        if (int(digits[i]) + int(digits[i+1])) % 2 != 0:
            return "Invalid"
    if letter in "AEIOUY":
        return "Invalid"
    return "Valid"
tag = '24B678-90'
print(is_valid_tag(tag))

def is_valid_tag(tag):
    # Check if the tag length is 9
    if len(tag) != 9:
        return "Invalid"

    # Extract digits and letter from the tag
    digits = tag[:2] + tag[3:6] + tag[7:9]
    letter = tag[2]

    # Check if the sum of every two consecutive digits is even
    for i in range(0, 8, 2):
        if (int(digits[i]) + int(digits[i+1]))%2!=0:
            return "Invalid"

    # Check if the letter is not a vowel
    if letter in "AEIOUY":
        return "Invalid"

    # If all conditions are met, the tag is valid
    return "Valid"

# Input
tag = '24B678-90'

# Output
print(is_valid_tag(tag))



a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in range(0, len(a)):
    if a[i]==9:
        continue
    b.append(a[i])
print(b)

a=[1,2,3,0,0,98]
c=[]
d=[]
for i in range(len(a)):
    if a[i]!=0:c.append(a[i])
    else:d.append(a[i])
c.extend(d)
print(c)

a='sanjay'
b=list(a)
for i in b:
    b[5]='k'
print(b)

a='023qwerty'
b='0123456789wertyuiopqasdfghjklnbvcxz'
c=[]
for i in b:
    if i not in a:
        c.append(i)
print(''.join(c))

a=[4,5,6,7,8,9]
for i in range(0,len(a),2):
    print(a[i+1],a[i],end=" ") 


a='A1B2cE'
c=[]
b=[]
for i in a:
    if i.isalpha():
        c.append(i)
    else: 
        b.append(i)
d=c+b
print(''.join(d))

a='sanjay'
print(a.strip('san'))

a='sanjay dharun yadav'
b=a.split()
for i in b:
    if len(i)%2==0:
        print(i)

a='Geeks123For123Geeks'
b=[]
for i in a:
    if i.isalpha():
        b.append(i)
print(*b)

myDict = {'ravi': 10, 'rajnish': 9,
		'sanjeev': 15, 'yash': 2, 'suraj': 32}
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
print(sorted_dict)

a= [10,20,30,40]
b=0
for i in a:
    b+=1
    print(b)

a='ASsasewWssadaweersdl'
b="AEIOUaeiou"
for char in a:
    if char in b:
        print(char.swapcase(), end='')
    else:
        print(char, end='')

a='ProSoccer'
b=a[::-1]
print(b[:-1]+b[-1:].lower(),end="")


a='11100011'
b=True
for i in a:
    if i not in ['1','0']:b=False
if b:print("True")
else:print("False")

def selectionSort(array, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print(arr)

a='ufjbhfdbffdhhj6hbjfhbgfh8$!'
b='wertyuiopolkjhgfdszxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,'
d='!@#$%^&*()'
c=[]
e=[]
for i in a:
    if i in b: 
        c.append(i)
    elif i in d:
        e.append(i)
print(''.join(c[::-1]+e))

def count_substring(string, sub_string):
        x = len(sub_string)
        c = 0
        for i in range(len(string)-len(sub_string)+1):
                if string[i:x+i] == sub_string:
                        c +=1
        return c
a='ABCDCDC'
B='CDC'
print(count_substring(a,B))

a={
    'a':'sanjay'
}
inverted={j:i for i,j in a.items()}
print(inverted)

a='abcdcdc'
b='cdc'
c=0
d=len(b)
for i in range(len(a)-len(b)+1):
    if a[i:d+i]==b:
        c+=1
print(c)

with open("viewspex.txt","w") as file:
    file.write('Hello')

a=''
b='!@#$%^&*()'
c='1234567890'
d='ASDFGHJKLMNOPQRSTUVWXYZabcdefghijkmn'
if len(a)<=16:
        if a not in b:
            print("Strong")
        else:
            print("Weak")
else:
    print("Sry")

a=[[1,2,3],[4,5,6],[7,8,9]]
b=list(map(lambda *a:sum(a),*a))
print(b)

a='q#nent,r@!'
b='aeiou'
c=[]
d=[]
for i in a:
    if i in ['!','@']:
        c.append(i)
for i in a[::-1]:
    if i in 'qwertyuiopasdfghjklzxcvb#nm,':
        d.append(i)
print(''.join(d+c))

a='sanjay ar a bad boy'
b=a.split()
for i in b:
    if len(i)>3:
        opt=i[0].lower()+i[1].upper()+i[2:-1].lower()+i[-1].lower()   
        print(''.join(sorted(opt[::-1])),end=" ")
    elif len(i)==1:
        opt=i.upper()
        print(opt[::-1],end=" ")
    elif len(i)==2:
        opt=i[0].lower()+i[1].upper()
        print(opt[::-1],end=" ")
    else:
        len(i)==3
        opt=i[0].lower()+i[1].upper()+i[2].lower()
        print(opt[::-1],end=" ")

def square(n):
    return int(n)**0.5
a=36
print(square(int(a)))

a=5
for i in range(0,11):
    print(a,"*",i ,'=',a * i)

a = 'gfg'
c = []
d = []
e = []
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
print("Unique characters:", c)
for j in range(len(a)-1):
    combination = a[j:j+2]
    if combination not in d:
        d.append(combination)
print("Unique two-character combinations:", d)
for k in range(len(a)-2):
    combination = a[k:k+3]
    if combination not in e:
        e.append(combination)
print("Unique three-character combinations:", e)



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(my_list)
print(''.join(my_list))

def insertion(arr):
    for i in range(1,len(arr)):
        b=i
        while b>0 and arr[b]<arr[b-1]:
            arr[b],arr[b-1]=arr[b-1],arr[b]
            b-=1
    print(arr)
a=[7,6,54,63,5]
insertion(a)
for i in a:
    print(i,end=" ")


def find_gcd(x, y):
    while y:
         x,y = y,x % y
    return x
def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)
num1 = 12
num2 = 18
lcm_result = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm_result}")


def selectionSort(array, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print(arr)


def gcd(x,y):
    while y:
        x,y=y,x%y
    return x
def lcm(a,b):
    return (a*b)  // gcd(a,b)
n=3
n2=10
print(f'{n} and {n2}',gcd(n,n2))
print(lcm(n,n2))

a=str(input())
b=a.split()
print(b)
c=sorted(b)
print(c)
print(''.join(c[::-1]))'''

'''a=input().split()
z=''
max(a)
v=len(max(a,key=len))
print(v)
c=sorted(a,key=lambda x:x[0])
print(c)
for i in range(len(c)-1,-1,-1):
    z+=c[i]
print(z)

def selectionSort(arr,size):
    for i in range(size):
        min=i
        for j in range(i+1,size):
            if arr[j]<arr[min]:
                min=j
                arr[i],arr[min]=arr[min],arr[i]
    return arr
a=[98,65,32,769,8]
size=len(a)
print(selectionSort(a,size))

a=[11,2,3,0,0,4,5]
for i in a:
    if i == 0:
        a.remove(i)
        a.append(i)
print(a)


a=list(map(int,input().split()))
mid=len(a)//2
c=sorted(a[:mid])
print(c)
d=sorted(a[mid:],reverse=True)
print(d)
print(c+d)

a=[8,4,2,1]
sum=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j] and i < j:
            sum+=1
print(sum)


def insertion(a):
    for i in range(1,len(a)):
        b=i
        while b>0 and a[b]<a[b-1]:
                a[b],a[b-1] =a[b-1],a[b]
                b=b-1
    return a

a="sanjay"
n='s','a'
d=dict()
for i in n:
    d[i]=a.count(i)
print(d)

a="sanjay"
b='aeiouAEIOU'
c=sum(a.count(i) for i in b)
print(c)

a=[2,1,2,5,7,1,9,3,6,8,8]
b=[2,1,8,3]
c=[]
d=[]
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[j]:
            c.append(a[j])
for j in range(len(a)):
    if a[j] not in c:
        d.append(a[j])
print(c+sorted(d))

a=[1,0,3,2]
b=sorted(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]-a[j]==1 and a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
if a == b:
    print("Yes")
else:
    print("No")


a=input().split()
b=input().split()
c=dict()
for i in b:
    c = a.count(i)
print(c)

a=[2,3,1,3,4]
a.sort()
print(*a)

a=[2,3,1,4,4,4,4]
for i in range(len(a)):
    if a.count(i)>len(a)//2:
        print(a[i])

a=[2,2,0,3,8,1,1,3,41]
b=[2,1,3]
c=[]
d=[]
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[j]:
            c.append(a[j])

for j in range(len(a)):
    if a[j] not in c:
        d.append(a[j])
print(c+d)

a=[10,5,6,3,2,20,100,80]
for i in range(1,len(a)-1):
    if i%2!= 0:
        if  a[i-1] < a[i]: 
            a[i],a[i-1]=a[i-1],a[i]
        if a[i] > a[i+1] : 
            a[i+1],a[i]=a[i],a[i+1]
print(*a)


a=[10,1,2,3]
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        a[i],a[i+1] = a[i+1],a[i]
print(a)


a=[10,5,6,3,2,20,100,80]
#Output 10 5 6 2 20 3 100 80
for i in range(1,len(a)-1):
    if i%2!=0:
        if a[i-1]<a[i]:
            a[i],a[i-1]=a[i-1],a[i]
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(*a)

a='ProScoccer'
b=a[::-1]
print(b[:-1]+b[-1].swapcase())

a=[0,1,1,0,1,2,2,0,1]
b=['a','b','c','d','e','f','g','h','i']
c=zip(a,b)
d=sorted(c)
print(d)
for i in c:
    print(i,end="")

a=[1,5,6,9,11]
b=[3,4,7,8,10]
print(sorted(a+b))'''

'''from itertools import combinations
a='geeks'
b=combinations(a,3)
c=[''.join(i) for i in b]
print(c)

a='mommy'
b=''
for i in a:
    if i not in b:
        b+=i
print(b)

def reverse_string_with_special_characters(s):
    s_list = list(s)
    left, right = 0, len(s_list) - 1
    while left < right:
        while left < right and not s_list[left].isalnum():
            left += 1
        while left < right and not s_list[right].isalnum():
            right -= 1
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    result = ''.join(s_list)
    return result
input_str = "abc@,iu!$"
output_str = reverse_string_with_special_characters(input_str)
print(output_str)


a=5
for i in range(a):
    for j in range(a):
        if i==j:
            print("1",end="")
        else:
            print("0",end="")
    print()

a=[1,2,3,4]
target=7
b=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
            b.append(a[i])
            b.append(a[j])
print(b)

a=int(input())
l=[]
while a!=0:
    r=a%2
    l.append(r)
    a=a//2
l.reverse()
for i in l:
    print(i)

def f(c):
    return True if c==str(c) else False
a='sanjay'
print(f(a))

a=[23,32,324,2111,11111]
b=2
c=0
while a:
    mid=(len(a)-1)//2
    if b==a[mid]:
        c=1
        break
    elif b>a[mid]:
        a=a[mid+1:]
    elif b<a[mid]:
        a=a[:mid]
if c==1:
    print("S")
else:
    print("N")

    
a=input().split()
for i in range(len(a)):
    if a[0]==a[-1]:
        print("Matched")
        break
    else:
        print("Not matched")
        break

a=input().split()
b=[]
c=a.pop()
b.append(b)
d=str(b)
print(len(c))

def rotate(a,n):
    a=a[-n:]+a[:-n]
    return a
a=list(map(int,input("Enter:").split()))
n=int(input("Enter a rotation:"))
print(rotate(a,n))


a=[1,2,3,4,5]
b=1
c=0
while a:
    mid=(len(a))//2
    if b==a[mid]:
        c=1
        break
    if b>a[mid]:
        a=a[mid+1:]
    elif b<a[mid]:
        a=a[:mid]

if c==1:
    print('s')
else:
    print('NO')


a="sanjay dharun yadav"
c=a.split()[::-1]
print(*c)

a= input().split()
b= '[],(),{}'
for i in a:
    if i in b:
        print("Valid")
    else:
        print("Invalid")

def s(a):
    b=''
    for i in a:
        if i not in b:
            b+=i
        else:
            return False
    return True
a="momy"
print(s(a))

a='yabcaabcbabccyabcabz'
b='abc'
while (b in a):
    c=a.find(b)
    a=a[0:c]+a[c+len(b):]
    print(a)

a=[13,2,4,15,12,10,5]
b=[]
c=[]
d=[]
for i in range(len(a)):
    if i%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
b.sort(reverse=True)
c.sort()
print(b)
print(c)
c.append(0)
for j in range(len(c)):
    d.append(b[j])
    d.append(c[j])
d.pop()
print(d)


a=[5,4,2,21,4]
b=[6,7,5,3,22]
d=[]
n=0
for i in range(5):
    g=a[i]-b[i]
    n=n+g
    d.append(n)
print(max(d))

a=['r','b','b','b','c','c']
b=[]
c=[1,3,5,7]
for i in range(len(a)):
    if a.count(a[i])==1 or a.count(a[i])==3:
        b.append(a[i])
print(b)


a=[5,4,2,21,4]
b=[6,7,5,3,22]
d=[]
n=0
for i in range(5):
    g=a[i]-b[i]
    n=n+g
    d.append(n)
print(max(d))

a=10
print(bin(a))

a=int(input())
n=[]
while a:
    r=a%2
    n.append(r)
    a=a//2
n.reverse()
for i in n:
    print(i,end="")

class Sanjay:
    x=0
    def sum(self):
        x=x+1
        print(x)
sam=Sanjay()
print(type(sam))
print(dir(sam))

class Sanjay:
    x=0
    def __init__(self):
        print("Constructor")
    def Party(self):
        self.x=self.x+1
        print("So far",self.x)
    def __del__(self):
        print("So far")

san=Sanjay()
san.Party()
san.Party()
san="Sanjay"
print(san)

print("Welcome to Sanjay ATM!!!")
User_Account_Pin=int(input("PLease Enter Your Account Pin:"))
depsoit=5000
if User_Account_Pin == 1234:
    print(" Please Enter Your Query:")
    dep=depsoit+depsoit
    Query=str(input())
    if Query=="Withdraw":
        Balance=print("Your Total balance is:",depsoit)
        print("Your Available Balance According to Bank:",depsoit-1000)
        Withdraw=int(input("PLease Enter Your Withdraw Amount:"))
        print("Bank Balance After Withdraw:",depsoit-Withdraw)
        print("Thank You")

    elif Query=="Deposit":
        depsoit=int(input("Enter the Amount You Need To Deposit:"))
        dep=0+depsoit
        print("Your Depsoit Amount is:",dep)
    elif Query=="Mini Statement":
        print("24.09.2024 ==> Paid to Rathinam TEchnical Campus") 
        print("23.09.2024 ==> Paid to Jio Recharge") 
        print("22.09.2024 ==> Paid to Amma")
        print("22.09.2024 ==> Paid to Appa")    
    elif Query=="Balance Enquiry":
        print("Your Balance Amount is:",depsoit)
else:
    print("Your Account Pin is Wrong/Invalid")


class ATM:
    def __init__(self):
        print("Welcome To The SGSD Bank ATM!!!")
        print("PLEASE ENTER THE 4 DIGIT PIN")
        print("1 ==> Deposit")
        print("2 ==> Withdraw")
        print("3 ==> Mini Statement")
        print("4 ==> Balance Enquiry")
    def Account(Account_Pin):
        while True:
            depsoit=57890.70
            Account_Pin=int(input("Enter the PIN:"))
            if Account_Pin == 1234:
                print(" Please Enter Your Query:")
                Query=int(input())
                if Query==1:
                    print('Depsoit')
                elif Query==2:
                    print('Withdraw')
                elif Query==3:
                    print("Mini Statement")
                elif Query==4:
                    print("Balance Enquiry")
                else:
                    print("Sry")
                if Query==2:
                    print("Your Total balance is:",depsoit)
                    print("Our Minimum Balance is Rupees ==> 1000")
                    print("Your Available Balance According to Bank:",depsoit-1000)
                    Withdraw=int(input("PLease Enter Your Withdraw Amount:"))
                    print("Bank Balance After Withdraw:",depsoit-Withdraw)
                    print("Thank You")
                    oper=str(input("You Need to do Another Operation:"))
                    if oper=="Yes":
                        print("Ok")
                    else:
                        print("Thank you")     
                        break 
                elif Query==1:
                    depsoit1=int(input("Enter the Amount You Need To Deposit:"))
                    depsoit=depsoit+depsoit1
                    print("Your Depsoit Amount is:",depsoit)
                    print("You Need to do Another Operation:")
                    oper=str(input())
                    if oper=="Yes":
                        print("Ok")
                    else:
                        print("Thank you")     
                        break                   
                elif Query==3:
                    print("24.09.2024 ==> Paid to Rathinam Technical Campus") 
                    print("23.09.2024 ==> Paid to Jio Recharge") 
                    print("22.09.2024 ==> Paid to Amma")
                    print("22.09.2024 ==> Paid to Appa")
                    oper=str(input("You Need to do Another Operation"))
                    if oper=="Yes":
                        print("Ok")
                    else:
                        print("Thank you")     
                        break 
                elif Query==4:
                    print("Your Balance Amount is:",depsoit)
                    oper=str(input("You Need to do Another Operation"))
                    if oper=="Yes":
                        print("Ok")
                    else:
                        print("Thank you")     
                        break 
            else:
                print("Your Account Pin is Wrong/Invalid")
sanjay=ATM()
sanjay.Account()

a="geekgeeksfor"
a.split()
print(a)
b=list(set(a))
print(len(b))


class ATM:
    def __init__(self,Account,Pin,Balance):
        self.Account=Account
        self.Pin=Pin
        self.Balance=Balance
        print("Welcome to ATM!!!")
        self.operation()
    def Deposit(self):
        deposit=int(input("Enter the Amount You Need to Deposit:"))
        print(deposit+self.Balance)
    def Withdraw(self):
        print("Important Information for Bank Minimum Balance is ==> 1000")
        withdraw=int(input("Enter the Amount You Need to withdraw:"))
        print("Your Total Balance is ",withdraw-1000)
        print("Your Available Balance is ",self.Balance-withdraw)
    def operation(self):
        print("1 ==> Deposit")
        print("2 ==> Withdrraw")
        print("Please Enter  Your 4 Digit Pin:")
        Pin=int(input())
        if Pin==1234:
            operation=int(input(("Enter your Queries:")))
        if operation==1:
            self.Deposit()
        elif operation==2:
            self.Withdraw()    
sanjay=ATM(122345,1234,50000)'''

'''class Movie:
    def __init__(self,Title,Director,Producer,Actor):
        self.Title = Title
        self.Director = Director
        self.Producer = Producer
        self.Actor = Actor
        print("Welcome to Movie Recommendation System!!!")
        self.Rating()
    def Movie(self):
        star=int(input("Rate the Star for Character and Performance(10 Star):"))
        star1=int(input("Rate the Star for Storytelling and Context(10 Star):"))
        star2=int(input("Rate the Star for Pace and Effect(10 Star):"))
        star3=int(input("Rate the Star for Sound Track(10 Star):"))
        star4=int(input("Rate the Star for Cinematography(10 Star):"))
        rat=star+star1+star2+star3+star4
        print(rat)
        return rat
    def Dialogue(self):
        star1=int(input("Rate the Star for Character and Performance(10 Star):"))
        print(star1)
    def Editing(self):
        star2=int(input("Rate the Star for Character and Performance(10 Star):"))
        print(star2)
    def Rating(self):
        rating=self.Movie()
        if (rating) >= 10 and (rating)<25:
            print("Average")
        elif (rating)>=25 and (rating)<35:
            print("Watchable")
        elif (rating)>=35 and (rating)<45:
            print("Recommended")
        elif (rating)>=45 :
            print("Highly Recommended")
sanjay=Movie("KKM","SS","SD","Kumar")'''

'''class Hotel_Reservation:
    def __init__(self,Check_in,Check_out):
        self.Check_in=Check_in
        self.Check_out=Check_out
        print("Welcome to the Lilac hotel!!!")
        self.Processing()
    def Search(self):
        print("Welcome to the Booking Option!!!")
        print("Available Rooms are ==> 201",'122','765','980')
        print("If you need to Continue: ")
        con=str(input())
        if con=="Yes":
            self.Processing()
        elif con=="No":
            print("Thank You For Visiting Us")
    def Reservation(self):
        print("Your Check_in Date is ==>",self.Check_in)
        print("Your Check_Out Date is ==>",self.Check_out)
        print("Available_Rooms:201,122,76,80")
        Available_Rooms=int(input("Plese Enter the Available Room Number:"))
        if Available_Rooms=="201" or'122'or'76'or'80':
            Amount=str(input("Upi or NetBanking"))
            if Amount=="Upi":
                print("Payment Done")
                print("Thanks For Booking!!!")
                print("Your Room Number is ==> ",Available_Rooms)
            else:
                print("Thanks For Booking")
        else:
            print("Room is Not Available")
    def Modify(self):
        Name=str(input("Enter the Name of the Room Booked:"))
        if Name=="Sanjay":
            print("Your Booked Room is",)
            M_check_in=str(input(("Enter the Modify Check in Date:")))
            M_check_Out=str(input(("Enter the Modify Check Out Date:")))
            if self.Check_in==M_check_in:
                print("Already Booked in that Date Only")
            else:
                print("Your Old Check_in Date is ==>",self.Check_in)
                print("Your Old Check_Out Date is ==>",self.Check_out)
                print("Your Old Modify Check_in Date is ==>",M_check_in,)
                print("Your Old ModifybCheck_Out Date is ==>",M_check_Out)
        else:
            print("Sry Room number is Wrong")
    def Processing(self):
        Query=int(input("Enter Query:"))
        if Query== 1:
            self.Search()
        elif Query==2:
            self.Reservation()
        elif Query==3:
            self.Modify()
        else:
            print("Sry Option Not Available")
roo=Hotel_Reservation(12,14)'''

'''Boy_Name='pradeoep'
Girl_Name="Noor"
for i in Boy_Name:
    if i in Girl_Name:
        Boy_Name=Boy_Name.replace(i,'')
        Girl_Name=Girl_Name.replace(i,'')
print(Boy_Name)
for t in Girl_Name:
    if t in Boy_Name:
        Girl_Name=Girl_Name.replace(t,'')
        Boy_Name=Boy_Name.replace(t,'')
print(Girl_Name)
count=len(Boy_Name)+len(Girl_Name)
e=["F","L","A","M","E","S"]
while len(e)>1:
        ind= (count%len(e)) - 1
        if ind>=0:
            right=e[ind+1:]
            left=e[:ind]
            e=right+left
        else:
            e=e[:len(e)-1]
print(e)

arr=[7,69,2,221,8974]
print(sum(arr[0:len(arr)-1]))
print(sum(arr[1:len(arr)+1]))

def Selecion(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr
arr=[3,2,5,5,79,9]
print(Selecion(arr))

class Parent:
    def __init__(self,name):
        self.name=name
    def Sakthivel(self):
        print("This is a parent")
class Child(Parent):
    def __init__(self,name):
        super().__init__(name)
        self.name=name
    def Sanjay(self,name):
        self.name=name
        print("This is a child")
sak=Parent("Sakthivel")
san=Child("Sanjay")
print("Parent",sak.name)
print("Child",san.name)


class Animal:
    def sound(self):
        print("Oooooooo")
class Dog(Animal):
    def sound(self):
        print("Boww Bowwww")
class Cat(Animal):
    def sound(self):
        print("Meow")

Animal=[Dog(),Cat()]
for i in Animal:
    i.sound()

a=str(input("Enter:"))
sum=0
for i in a:
    sum+=int(i)**len(a)
if int(a)==sum:
    print("Am")
else:
    print("NA")

#Lagguage Sum
a=[1,2,3,6,4]
b=4
c=0
for i in a:
    if i<=b:
        c+=1
    else:
        c+=2
print(c)


integer=int(input())
people=list(map(int,input().split()))
height=list(map(int,input().split()))
c=0
for i in range(len(people)):
    if people[i]<=height[0]:
        c+=1
    else:
        c=0
print(c)

def selection(arr):
    for i in range(0,len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
a=["34","4","6"]
c=[]
for i in a:
    c.append(int(i))
print(selection(c))

def bubble(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=[5,6,8,43,899,99]
print(bubble(arr))

a=[[1,2,3],
   [4,5,6],
   [6,7,8]]
temp=0
cemp=0
for i in range(len(a)):
    temp=temp+a[i][i]
print(temp)
for j in range(len(a)):
    cemp=cemp+a[j][len(a)-j-1]
print(cemp)


a='0101010'
b=True
for i in a:
    if i not in ['0','1']:
        b=False
if b:print("True")
else:print("False")


a=[[1,2,3],
   [4,5,6],
   [6,7,8]]
c=0
for i in range(len(a)):
    c+=a[1][i]
print(c)

a='aeiou'
b=True
for i in a:
    if i not in ['a','e','i','o','u']:
        b=False
if b:print("True")
else:print("False")

a="sanjay"
b="s","a"
d=dict()
for i in b:
    d[i]=a.count(i)
print(d)

a="sanjau"
b="aeuio"
c=""
d=""
for i in a:
    if i in b:
        c+=i
print("Vowel Present In Words:",c)
for i in a:
    if i not in b:
        d+=i
print("Vowel Present Not In Words:",d)

def selection(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]: 
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr
arr=[8,5,3,2,67,70]
print(selection(arr))


a=[1,2,3,4,5,6,7]
b=[1,2,3,4,5,6,7]

for i in zip(a,b):
    print(i,end=" ")

a=22112323
print(f'{a:,}')

import math
a=4
b=4
c=3
s=(a+b+c)//2
print(math.sqrt(s*(s-a)*(s-b)*(s-c)))

a=int(input())
l=[]
for i in range(0,a):
    n=int(input())
    l.append(n)
print(l)

count=0
sum=0
while count<10:
    a=int(input("Enter a count:"))
    count+=1
    sum+=a
print(sum/count)

a=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(0,len(a),2):
    print(a[i+1],a[i],end=" ")

a="qwetqweryuqwe"
patter="qwe"
while (patter in a):
    c=a.find(patter)
    a=a[0:c]+a[c+len(patter):]
print(a)

def snake(t):
    for i in range(0,len(t)):
        if i%2==0:
            for j in t[i]:
                print(j,end=" ")
        else:
            for j in t[i][::-1]:
                print(j,end=" ")
    return t

t=[[1,2,3],[4,5,6],[7,8,9]]
print(snake(t))

def spiral_order(matrix):
    ans = []
    while matrix:
        ans += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                ans.append(row.pop())
        if matrix:
            ans += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ans.append(row.pop(0))
    return ans

# Example usage
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
print(spiral_order(matrix))

row= 5
c=5
cl=[]
for i in range(row):
    r=[]
    for j in range(c):
        n=int(input())
        r.append(n)
    cl.append(r)
print(cl)'''

'''class Quiz:
    def __init__(self,quiz,input):
        self.quiz=quiz
        self.input=input
        print("Welcome to Sanjay's Quiz!!!")
        self.processing()
    def Question(self):
        print("Please Enter Your Topic:")
        Topic=str(input())
        if Topic=="Python":
            print("Welcome to Python Quiz Your Questions Are:")
            print("Who is the Father of Python?")
            print("Options are \n a).Guido Van Russem b).Sanjay c).Yadav d).Kumar")
            Answer=str(input("Please Enter the Options: "))
            if Answer=="a":
                print("Good :) 10 Marks")
            else:
                print("Sry :(")
        else:
            print("Currently we are Processing")
    def processing(self):
        print("Enter Your Choice:")
        choice=int(input())
        if choice==1:
            self.Question()
        else:
            print("Sry Curretly We are processing")

Qui=Quiz(1,2)

a=[8,89,89,89]
b=[90,87,87,90]
Boys=sorted(a)
Girls=sorted(b)
for i in range(len(Boys)):
    for j in range(len(Girls)):
        if Boys[i]>=Girls[j]:
            print("True")
            break
        else:print("False")'''



'''class Animal:
    def Bird(self):
        print("Koo Koo")
    def Human(self):
        print("Hii")
    def Wild(self):
        print("Angry")
a=Animal()
a.Bird()
a.Human()
a.Wild()'''
'''
a="khokkhok"
mid=len(a)//2
if a[:mid]==a[mid:]:
    print("Symmetric")
else:print("Not a Symmetric")

a=[3,5,2,4,46,35,21,2,4,3]
b=sorted(a)
print("The Smallest Element in the List are:", b[0])

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return 1
    else:
        moves = 0
        moves += tower_of_hanoi(n-1, source, auxiliary, destination)
        print("Move disk", n, "from rod", source, "to rod", destination)
        moves += 1
        moves += tower_of_hanoi(n-1, auxiliary, destination, source)
        return moves 
n = 3
source_rod = 'A'
destination_rod = 'C'
auxiliary_rod = 'B'
total_moves = tower_of_hanoi(n, source_rod, destination_rod, auxiliary_rod)
print("Total number of moves:", total_moves)'''


'''Boy_Names = str(input("Enter the Boy Name: "))
Girl_Names = str(input("Enter the Girl Name: "))
for i in Boy_Names:
    if i in Girl_Names:
        Boy_Names = Boy_Names.replace(i, "", 1)
        Girl_Names = Girl_Names.replace(i, "", 1)
total = len(Boy_Names) + len(Girl_Names)
Flames = ["F", "l", "a", "m", "e", "s"]
while len(Flames) > 1:
    s = total % len(Flames) - 1
    if s >= 0:
        Flames = Flames[s + 1 :] + Flames[:s]
    else:
        Flames = Flames[: len(Flames) - 1]
result = Flames[0]
if result == "F":
    print("Friendship")
elif result == "L":
    print("Love")
elif result == "A":
    print("Affection")
elif result == "M":
    print("Marriage")
elif result == "E":
    print("Enemies")
elif result == "S":
    print("Sibling")'''

'''
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return 1
    else:
        moves = 0 
        moves += tower_of_hanoi(n-1, source, auxiliary, destination)
        print("Move disk", n, "from rod", source, "to rod", destination)
        moves += 1
        moves += tower_of_hanoi(n-1, auxiliary, destination, source)
        return moves 
n = 3
source_rod = 'A'
destination_rod = 'C'
auxiliary_rod = 'B'
total_moves = tower_of_hanoi(n, source_rod, destination_rod, auxiliary_rod)
print("Total number of moves:", total_moves)'''

'''for row in range(7):
    for col in range(5):
        if col==0 or col==4 or (row==3 and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=' ')
    print()'''

'''def Tower(n,Source,Destination, auxiliary):
    if n==1:
        return 1
    else:
        move=0
        move+=Tower(n-1,Source,auxiliary,Destination)
        move+=1
        move+=Tower(n-1,auxiliary,Source,Destination)
    return move
n=3
Source='A'
Destination='C'
Auxiliary="B"
print(Tower(n,Source,Destination, Auxiliary))'''


'''a=int(input("Enter the number:"))
if a<   1:
    print("Not a Prime")
elif a==2:
    print("Prime")
else:
    for i in range(2,(int(a)**5)+1):
        if a%i==0:
            print("Not a Prime")
            break
        else:
            print("Prime")
            break'''
'''matrix=[[1,2,3],
        [4,5,6],
        [7,8,9],
        [1,2,3]]
a=[]
while matrix:
    a+=matrix.pop(0)
    if matrix and matrix[0]:
        for i in matrix:
            a.append(i.pop())
    if  matrix:
        a+=matrix.pop()[::-1]
    if matrix and matrix[0]:
        a+=matrix.pop()
    if matrix and matrix[0]:
        for i in matrix:
            a.append(i.pop())
print(a)
'''
'''a=[2,2,0,4,0,8]
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        a[i]=2*a[i]
        a[i+1]=0
print(a)
for i in range(len(a)):
    if a[i]==0:
        a.remove(a[i])
        a.append(0)
print(a)'''


'''a=[7,0,5,1,3]
b=[1,2,1,3,4]
d=0
for i in range(len(a)):
    c=a[i]-b[i]
    d=d+c
print(d)'''

'''=int(input("Enter the Value:"))
b=str(input())
c=[]
for i in range(a):
    if b.count(b[i])==1 or b.count(b[i])==3:
        c.append(b[i])
print(c)
    '''
'''a=[2,2,0,4,0,8]
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        a[i]=a[i]*2
        a[i+1]=0
print(a)
for j in range(len(a)):
    if a[j]==0:
        a.remove(a[j])
        a.append(0)
print(a)'''


'''x='1010'
d=[]
y=0
''''''b=0
c=[]
for i in range(len(a)):
    c.append(int(a[i]))
for i in range(len(c)-1):
    if c[i]==c[i+1]:
        c[i+1]=1
        b+=1
    else:
        c[i+1]=0
        b+=1
print(b)'''
'''
for i in range(len(x)):
    d.append(int(x[i]))
print(d)
for i in range(len(d)-1):
    if d[i]==d[i+1]:
        if d[i]==0:
            d[i+1]=1
            y+=1
        else:
            d[i+1]=0
            y+=1
print(y)'''

'''1.Python code to verify every odd index in a list contains odd number and Even Index contains Even number.

Sample Input:

2 1 4 3 6 7 6 3

Sample Output:

True
'''

'''a = [2, 3, 4, 3, 10]
for i in range(0, len(a)):
    if i%2==0:
        if a[i]%2==0:
            continue
        else:
            print("False")
            break
else:
    print("True")'''

'''a=[3,1,1,1,3,5]
c=[]
for i in range(0, len(a)-1): 
    if a[i]==a[i+1]==a[i+2]:
        c.append(a[i])
print(*c)   '''     

'''a=[1,44,1,45,543,6]
mid=len(a)//2
opt=sorted(a[:mid])
opt2=sorted(a[mid:],reverse=True)
print(*opt,*opt2)'''

'''a="agdswsdsxgbhwjnjkikewnazvwfdxwftyywjkm"
b="aeiuo"
c=[]
for i in b:
    if i in a:
        oop=a.replace(i," ")
    print(oop)
    break'''

'''a="sanjay"
b="AEIUOaeiou"
for i in a:
    if i in b:
        d=a.replace(i," ")
print(d)'''

'''a=[1,2,3,0,9,9,7,8,90]
b=[]
c=[]
for i in a:
    if i==0:
        b.append(i)
    else:
        c.append(i)
c.extend(b)
print(c)'''

# a=[2,2,0,4,0,8]
# for i in range(0,len(a)-1):
#     if a[i]==a[i+1]:
#         a[i]=2*a[i]
#         a[i+1]=0
# for i in range(0,len(a)-1):
#     if a[i]==0:
#         a.append(0)
#         a.remove(a[i])
# print(a)

'''
def pattern(a,k):
    b=[]
    c=[]
    e=[]
    for i in range(0,len(a),k):
        if a[i]==a[i+1]==a[i+2]:
            b.append(a[i])
        elif a[i]!=a[i+1]!=a[i+2]:
            c.append(a[i])
            c.append(a[i+1])
            c.append(a[i+2])
        elif a[i]==a[i+1]!=a[i+2]:
            e.append(a[i])
            e.append(a[i+2])
    print(*b)
    print(*c)
    print(*e)
a=str(input("Please Enter the Input:"))
k=int(input("Enter the Range:"))
print(pattern(a,k))'''

'''
def pattern(a,k):
    for i in range(0,len(a),k):
        l=[]
        s=i
        for j in range(k):
            if a[s] not in l:
                l.append(a[s])
            s+=1
        print(*l) 
a="AAAGBBHHJYYY"
k=int(input())
pattern(a,k)'''

'''a="BCDDDEAAA"
b=set(a)
c=[]
for i in b:
    c.append(i)
print(sorted(c))'''

'''a="qwert%$#,y"
s=a.split()
string=""
special=""
for i in s:
    for j in i:
        if j.isalnum():
            string+=j
        else:
            special+=string[::-1]+j
            print(special)
            string=""
    rev=special+string[::-1]
print(rev)    
'''

'''a=set(map(int,input().split()))
b=list(a)
b.sort()
print("The Second Largest",b[-2])'''

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.head=None
class LinkedList:
    def __init__(self,temp):
        self.head=None
        self.temp=temp
    def Create(self,data):
        node=Node(data)
        if self.head ==None:
            self.head=node
            self.temp=node
        else:
            self.temp.next=node
            self.temp=self.temp.next
    def Print(self):
        cd= self.temp
        print(cd)
l=LinkedList(1)
l=LinkedList(1)
l=LinkedList(1)
l=LinkedList(1)
l.Print()
l.Print()
l.Print()
l.Print()'''


# class Node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.Temp=None
#     def Create(self,data):
#         node=Node(data)
#         if self.head ==None:
#             self.head=node
#             self.Temp=node
#         else:
#             self.Temp.next=node
#             self.Temp=self.Temp.next
#     def insert_Initial(self,data):
#         node=Node(data)
#         self.Temp=self.head
#         self.head=node
#         self.head.next=self.Temp

#     def insertion_Middle(self,data,position):
#         node=Node(data)
#         self.Temp=self.head
#         self.Temp1=self.Temp.next
#         while (position>2):
#             self.Temp=self.Temp.next
#             self.Temp1=self.Temp.next
#             position-=1
#         if  (position > 1):
#             self.Temp.next=node
#             node.next=self.Temp1
#         else:
#             a.insert_Initial(data)

#     def dele_initial(self):
#         self.Temp=self.head
#         del self.Temp

#     def Print(self):
#         self.Temp=self.head
#         while self.Temp:
#             print(self.Temp.data)
#             self.Temp=self.Temp.next

# a=LinkedList()
# n=int(input())
# for i in range(n):
#     ele=int(input())
#     a.Create(ele)
# a.Print()
# a.insert_Initial(31)
# a.Print()
# a.insertion_Middle(3,1)
# a.Print()
# a.dele_initial()
# a.Print()


# a="AAABCDDDF"
# k=3
# for i in range(0,len(a),k):
#     d=i
#     l=[]
#     for j in range(k):
#         if a[d] not in l:
#             l.append(a[d])
#         d+=1
#     print(*l)

'''a=[1,2,3,5,-1]
b=[]
for i in range(0,len(a)):
    if a[i] > 0:
        b.append(a[i])
c=b[0]
for j in range(len(a)):
    if c!=a[j]:
        print(c)
        break
    c+=1'''

# a=[111,112,113,115,-1]
# # a.sort()
# # a.pop(0)
# c=[]
# for i in range(1,max(a)):
#     if i not in a:
#         c.append(i)
# print(c.pop())

# class Node():
#     def __init__(self,data,next):
#         self.data = data
#         self.next = None
# class LinkedList():
#     def __init__(self):
#         self.head=None
#         self.Temp=None
#     def Create(self,data):
#         node=Node(data)
#         if self.head == None:
#             self.head=node
#             self.Temp=node
#         else:
#             self.Temp.next=node
#             self.Temp=self.Temp.next
#     def Print(self):
#         self.Temp=self.head
#         while self.Temp:
#             print(self.Temp.data)
#             self.Temp=self.Temp.next
# a=LinkedList()
# a.Create(11)
# a.Create(11)
# a.Create(11)
# a.Print()


# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList():
#     def __init__(self):
#         self.head = None
#         self.Temp = None
#     def Create(self, data):
#         node = Node(data)
#         if self.head ==None:
#             self.head = node
#             self.Temp = node
#         else:
#             self.Temp.next = node
#             self.Temp = self.Temp.next
#     def insert(self,data):
#         node=Node(data)
#         self.Temp=self.head
#         self.head=node
#         self.head=self.Temp
        
#     def Print(self):
#         self.Temp = self.head
#         while self.Temp:
#             print(self.Temp.data)
#             self.Temp = self.Temp.next
# a = LinkedList()
# a.Create(11)
# a.Create(11)
# a.Create(11)
# a.Print()
# a.insert(34)
# a.Print()


# class Signup():
#     # def __init__(self):
#         # self.email=email
#         # self.password=password
#     def Login(self):
#         op=input()
#         if op=="Signup":
#             print("Please enter your Email:")
#             email=str(input())
#             print("Enter your Password:")
#             password=str(input())
#             if password=="password" and email=="sanjay@gmail.com" :
#                 print("Permission Granted")
#             else:
#                 print("Email or Password is Werng")
#         else:
#             print("Access Denied")
# s=Signup()
# s.Login()

'''a=set(map(str,input().split()))
b=list(a)
print(b[-1])'''

'''a=[11,12,13,15,-1]
c=[]
for i in range(1,max(a)):
    if i not in a:
        c.append(i)
print(c.pop())'''


'''a="geeks"
c=[]
for i in range(len(a)-1,0,-1):
    c.append(a[i])
print(*c)'''

'''a=[1,2,3,4,5]
n=3
c=0
while a:
    mid=len(a)//2
    if a[mid]==n:
        c=1
        break
    elif a[mid]> n:
        a=a[:mid]
    elif a[mid]<n:
        a=a[mid+1:]
if c==1:
    print("True")
else:
    print("False")'''


'''u=[3,1,9,4,5,2]
u.sort()
print("the minimum number of",u[0])
print("The maximum number of",u[-1])'''

'''sanjay=["apple", "banana", "apple", "orange", "banana", "apple"]
dharun="apple","banana",'orange'
d=dict()
for i in dharun:
    d[i]=sanjay.count(i)
print(d)'''

'''a=[1,2,3,23,13,3,32,2,3,4,5,]
unique=[]

for i in a:
    if i not in unique:
        unique.append(i)
print(unique)
'''



# stock_Price=[7,1,5,3,6,4]
# to_buy=[]
# to_sell=[]
# stock_Price.sort()
# s=stock_Price[0]
# for i in stock_Price:
#     if s<i:
#         to_sell.append(i)
# for j in stock_Price:
#     if s>j:
#         to_buy.append(j)
#     else:
#         to_buy.append(1)
#         break
# print("Stock to Buy",min(to_buy))
# print("stock to sell",max(to_sell))
# # stock_Price1=[]
# '''for i in range(len(stock_Price)-1):
#     if stock_Price[i]<stock_Price[i+1]:
#         stock_Price1.append(stock_Price[i])
# print(stock_Price1)'''

# # for price in stock_Price:
# #     min_price = min(min_price, price)  # Update the minimum price if necessary
# #     max_profit = max(max_profit, price - min_price)
'''
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist():
    def __init__(self) -> None:
        self.head = None
        self.Temp = None
    def Create(self,data):
        node=Node(data)
        if self.head==None:
            self.head = node
            self.Temp = node
        else:
            self.Temp.next = node
            self.Temp=self.Temp.next
    def Insert_initially(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def Print(self):
        self.Temp=self.head
        while self.Temp:
            print(self.Temp.data)
            self.Temp=self.Temp.next
san=Linkedlist()
lin=list(map(int,input().split()))
for i in lin:
    san.Create(i)
san.Print()
san.Insert_initially(1)
san.Print()

'''

# arr=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# c=[]
# while arr:
#     c+=arr.pop(0)
#     if arr and arr[0]:
#         for i in arr:
#             c.append(i.pop())
#     if arr:
#         c+=arr.pop()[::-1]
# print(c)


# n=int(input())
# inner=[]
# for i in range(n):
#     outer=[]
#     for j in range(n):
#         ni=int(input())
#         outer.append(ni)
#     inner.append(outer)
# print(inner)



# a=[1,3,4,5,6,8,9]
# b=[1,5,8,9,2]
# c=[]
# d=[]
# e=[]
# f=[]
# for i in a:
#     if i not in e:
#         e.append(i)
# for i in b:
#     if i not in e:
#         e.append(i)
# print("Union",e)

# for i in a:
#     if i in b:
#         f.append(i)
# print("Intersection",f)
# set1=set(a)
# set2=set(b)
# set_union=set1.union(set2)
# set_inter=set1.intersection(set2)
# print("The union Value are",set_union)
# print("The interscetion:",set_inter)
# for i in a:
#     if i%2!=0:
#         c.append(i)
# for i in b:
#     if i%2==0:
#         d.append(i)
# print("Except",c+d)

# a=[0,-1,2,-3,1,-2]
# n=3
# count=0
# for i in range(0,len(a),n):
#     if a[i]-a[i+1]-a[i+2]==0:
#         count+=1
# print(count)

'''from itertools import combinations
a=[0,-1,2,-3,1,-2]
c=list(combinations(a,3))
count=0
for i in c:
    if sum(i)==0:
        count+=1
print(count)'''

'''a='010j1010101'
b=True
for i in a:
    if i not in ["0","1"]:
        b=False
if b:print("True")
else:print("False")'''
'''
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
        self.Temp = None
    def Create(self, data):
        node = Node(data)
        if self.head ==None:
            self.head = node
            self.Temp = node
        else:
            self.Temp.next = node
            self.Temp = self.Temp.next
    def insert(self,data):
        node=Node(data)
        node.next = self.head
        self.head = node
    def Print(self):
        self.Temp=self.head
        while self.Temp:
            print (self.Temp.data)
            self.Temp=self.Temp.next
a=LinkedList()
a.Create(1)
a.Print()
a.insert(3)
a.Print()'''


'''a=[1,2,3,4,5,6,7,8,9]
b=[9,8,7,6,5,4,3,2,1,0]
union=[]
intersection=[]
#Union
for i in a:
    if i not in union:
        union.append(i)
for i in b:
    if i not in union:
        union.append(i)
print(union)
#Intersection
for i in a:
    if i in b:
        intersection.append(i)
print(intersection)'''



# def insertion(arr):
#     for i in range(2,len(arr)):
#         b=i
#         while b>0 and arr[b]<arr[b-1]:
#             arr[b],arr[b-1] = arr[b-1],arr[b]
#             b-=1
#     print(arr)
# a=[4,24,523,52,5,45,4]
# insertion(a)

# def bubble (arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#     print(arr)
# a=[2,34,2,34,23,4,32,3,2,4]
# bubble(a)

# a=(input("Enter Your Name:"))
# b=""
# c=a[0]
# for i in range((len(a)-1),0,-1):
#     b+=(a[i])
# print(b+c)

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# b=int(input("Enter a Range of 1st"))
# c=int(input("Enter a Range of 1st"))
# d=[]
# for i in range(len(a)):
#     if a[b]:
#         d.append(a[b])
#         d.append(a[c])
# print(d)


"""a=[11,12,13,15,-11]
c=[]
for i in range(0,max(a)):
    c.append(i)
print(c.pop())"""

# a="AAABCDDDF"
# for i in range(0,len(a),3):
#     c=[]
#     s=i
#     for j in range(3):
#         if a[s] not in c:
#             c.append(a[s])
#         s+=1
#     print(c)



#print(a[b:c]) 

# a=[1,2,3,4,5]
# n=int(input("Enter:"))
# for i in a:
#     o=a[-n:]+a[:-n]
# print(o)

# a=[[1,2,3,12],
#    [4,5,6,34],
#    [7,8,9,89],
#    [1,2,3,12]]
# c=[]
# while a:
#     c+=a.pop(0)
#     if a and a[0]:
#         for i in a:
#             c.append(i.pop())
#     if a:
#         c+=a.pop()[::-1] 
#     if a:
#         c+=a.pop()
#     if a:
#         c+=a.pop()[::-1]
# print(c)

# # c=0
# print(Peru(a))

#     # if sum(i)==0:
#     #     c+=1 
# # print(c)


# a = [1, -1, 0,0,3,4,4]
# c = []
# for i in range(len(a)):
#     first = a[i]
#     remaining = a[:i] + a[i+1:]
#     for j in range(len(remaining)):
#         second = remaining[j]
#         last = remaining[:j] + remaining[j+1:]
#         for k in last:
#             if first + second + k == 0:
#                 c.append([first, second, k])
# f=0
# for i in c:
#     if sum(i)==0:
#         f+=1
# print(f)


'''from  itertools import combinations
a=[1,-1,0,8,9,2]
c=0
n=list(combinations(a,3))
print(n)
for i in n:
    if sum(i)==0:
        c+=1
print(c)
'''

# a=[1,45,65,234,65,24]
# c=[]
# for i in range(len(a)):
#     first=a[i]
#     rem=a[:i]+a[i+1:]
#     for j in range(len(rem)):
#         sec=rem[j]
#         rem2=rem[:j]+rem[j+1:]
#         for k in rem2:
#                 c.append([first,sec,k])
# print(c)




# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.temp=None
#     def create(self,data):
#         node=Node(data)
#         if self.head == None:
#             self.head=node
#             self.temp=node
#         else:
#             self.temp.next=node
#             self.temp=self.temp.next
#     def print(self):
#         self.temp=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
#     def insert(self,data):
#         node=Node(data)
#         node.next=self.head
#         self.head=node
# san=LinkedList()
# l=list(map(int,input().split()))
# for i in l:
#     san.create(i)
# san.print()
# san.insert(2)
# san.print()


'''a=[1,2,3]
c=[]
for i in range(len(a)):
    first=a[i]
    ram=a[:i]+a[i+1:]
    for j in range(len(ram)):
        sec=ram[j]
        last=ram[:j]+ram[j+1:]
        for k in last:
            c.append([first,sec,k])
print(c)'''

'''a=[1,2,3,54,53,241,3,2,5,23,5,32,53,2,65,3]
n=51
c=0
while a:
    mid=len(a)//2
    if a[mid]==n:
        c=1
        break
    elif a[mid]>n:
        a=a[:mid]
    elif a[mid]<n:
        a=a[mid+1:]
if c==1:
    print("F")
else:
    print("N")'''
'''
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class D_LinkedList:
    def __init__(self):
        self.temp1=None
        self.temp2=None
        self.head=None
    def Create(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            self.temp1=node
            self.temp2=node
        else:
            self.temp1.next=node
            self.temp1.next=self.temp1
            self.temp1.prev=self.temp2
            self.temp2=self.temp1
    def insert_begin(self,data):
        node=Node(data)
        node.next=self.head
        self.head.prev=node
        self.head=node
    def insert_end(self,data):
        node=Node(data)
        self.temp2.next=node
        node.prev=self.temp2
        self.temp2=node
    def delete_begin(self):
        self.temp1=self.head
        self.head=self.head.next
        self.head.prev=None
        del self.temp1
    def delete_end(self):
        self.te=self.temp2
        self.temp2=self.temp2.prev
        self.temp2.next=None
        del self.te
    def print(self):
        self.temp1=self.head
        while self.temp1:
            print(self.temp1.data)
            self.temp1=self.temp1.next
        
sanjay=D_LinkedList()
sanjay.Create(1)
sanjay.print()
sanjay.insert_begin(9)
sanjay.insert_end(56)
sanjay.print()
# sanjay.delete_end()
# sanjay.print()'''




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.temp = None

#     def create(self, data):
#         node = Node(data)
#         if self.head == None:
#             self.head = node
#             self.temp = node
#         else:
#             self.temp.next = node
#             self.temp = self.temp.next

#     def insert_begin(self, data):
#         node = Node(data)
#         node.next = self.head
#         self.head = node

#     def delete_begin(self):
#         if self.head is not None:
#             self.head = self.head.next

#     def insert_last(self, data):
#         node =Node(data)
#         self.temp=self.head
#         while self.temp.next:
#             self.temp=self.temp.next
#         self.temp.next=node



#     def print(self):
#         self.temp = self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp = self.temp.next

# sanj = LinkedList()
# sanj.create(3)
# sanj.print()  # Output: 3
# sanj.insert_begin(2)
# sanj.insert_last(89)
# sanj.print()  # Output: 2 3 89

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            self.temp=node
        else:
            self.temp.next=node
            self.temp=self.temp.next
    def insert_begin(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def insert_last(self,data):
        node=Node(data)
        self.temp=self.head
        while (self.temp.next):
            self.temp=self.temp.next
        self.temp.next = node

    def delete_begin(self):
        self.head=self.head.next
    
    def delete_last(self):
        self.temp = self.head
        while self.temp.next.next:
            self.temp = self.temp.next
        self.temp.next = None
    
    def print(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data)
            self.temp=self.temp.next

a=LinkedList()
a.create(1)
a.print()
a.insert_begin(4)
a.insert_last(9)
a.delete_begin()
a.delete_last()
a.print()
'''


# class Node:
#     def __init__(self,data):
#         self.prev=None
#         self.data=data
#         self.next=None
# class D_linkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.temp=None
#     def create(self,data):
#         node=Node(data)
#         if self.head==None:
#             self.head=node
#             self.temp=node
#             self.tail=node
#         else:
#             self.tail.next=node
#             self.tail=self.tail.next
#     def insert_begin(self,data):
#         node=Node(data)
#         node.next=self.head
#         self.head=node
#     def Print(self):
#         self.tail=self.head
#         while self.tail:
#             print(self.tail.data)
#             self.tail=self.tail.next
# a=D_linkedlist()
# a.create(3)
# a.insert_begin(45)
# a.Print()

# a="sanjay"
# b="aeiou"
# for i in a:
#     if i in b:
#         opt=a.replace(i," ")
# print(opt)       



'''a = [1, 2, 3]
c = []
for i in range(len(a)):
    first = a[i]
    s = a[:i] + a[i+1:]
    for j in range(len(s)):
        sec = s[j]
        last = s[:j] + s[j+1:]
        for k in last:
            c.append((first, sec, k))
print(c)
'''




# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head = None
#         self.temp = None
#     def create(self,data):
#         node=Node(data)
#         if self.head == None:
#             self.head=node
#             self.temp=node
#         else:
#             self.temp.next=node
#             self.temp=self.temp.next
#     def print(self):
#         self.temp=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
# san=linkedlist()
# jay=linkedlist()
# list1=list(map(int,input().split()))
# list2=list(map(int,input().split()))
# for i in list1:
#     san.create(i)
# for j in list2:
#     jay.create(j)
# san.print()
# jay.print()
# c=list1+list2
# print(sorted(c))




# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head = None
#         self.temp = None
#     def create(self,data):
#         node=Node(data)
#         if self.head == None:
#             self.head=node
#             self.temp=node
#         else:
#             self.temp.next=node
#             self.temp=self.temp.next
#     def insert_bedgin(self,data):
#         node=Node(data)
#         node.next=self.head
#         self.head=node
    
#     def delete_begin(self):
#         self.head=self.head.next

#     def insert_end(self,data):
#         node=Node(data)
#         self.temp=self.head
#         while self.temp.next:
#             self.temp=self.temp.next
#         self.temp.next=node
    
#     def delete_last(self):
#         self.temp=self.head
#         while self.temp.next.next:
#             self.temp=self.temp.next
#         self.temp.next=None


#     def print(self):
#         self.temp=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
# a=linkedlist()
# a.create(1)
# a.create(2)
# a.create(3)
# a.insert_bedgin(3421)
# a.insert_end(1234)
# a.delete_begin()
# a.delete_last()
# a.print()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
# class D_linkedlist:
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None
#         self.temp=None
#     def create(self,data):
#         node=Node(data)
#         if self.head == None:
#             self.head = node
#             self.tail = node
#             self.temp = node
#         else:
#             self.temp.next=node
#             self.temp=self.temp.next
#     def insert(self,data):
#         node=Node(data)
#         self.head.prev=node
#         node.next=self.head
#         self.head=node
#     def print(self):
#         self.temp=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
# san=D_linkedlist()
# san.create(2)
# san.insert(1)
# san.print()

# a=6
# c=6
# for i in range(a):
#     for j in range(a):
#         if (i==0):
#             print(c-i,end="")
#         elif (j==0):
#             print(c,end="")
#         elif (i==5):
#             print(c,end="")
#         elif (i==1 and j==1) or (j==2 and i==1) or (j==3 and i==1) or (j==4 and i==1) :
#             print(c-i,end="")
#         elif ((j==1) and (i==2)) or (j==4 and i==2):
#             print(c-1,end="")
#         elif (i==2) and (j==2) or (i==2 and j==3):
#             print(c-2,end="")
#         elif ((j==1) and (i==3)) or (j==4 and i==3):
#             print(c-1,end="")
#         elif (i==3) and (j==2) or (i==3 and j==3):
#             print(c-2,end="")
#         elif (i==4) and (j==1) or (i==4 and j==2) or (i==4 and j==3) or (i==4 and j==4) :
#             print(c-1,end="")
#         elif (j==5):
#             print(c,end="")
#         elif (i==1 and j==5):
#             print(c,end="")
#     print()



# a="qwert%$#"
# s=a.split()
# for i in s:
#     string=""
#     special=""
#     for j in i:
#         if j.isalnum():
#             string+=j
#         else:
#             special+=string[::-1]+j
#             string=""
# print(special)

# a="AAABCDDDF"
# for i in range(0,len(a),3):
#     b=i
#     c=""
#     for j in range(3):
#         if a[b] not in c:
#             c+=a[b]
#         b+=1
#     print(c)

# from collections import Counter
# a=[1,2,3,2,1,2,3,423,44,24,43,5,63]
# frequencies=Counter(a)
# req=3
# if req in frequencies:
#     print(frequencies)
# else:
#     print("Sry")

'''
a=[1,2,3,4,5,15,6]
odd =[]
even=[]
total=[]
for i in range(0,len(a)):
    if i%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])
print(odd)
print(even)
odd.append(0)
odd.sort()
even.sort(reverse=True)
for j in range(len(even)):
    total.append(odd[j])
    total.append(even[j])
print(total)
'''

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class Circular_LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.temp=None
#     def create(self,data):
#         node=Node(data)
#         if self.head ==None:
#             self.head=node
#             self.tail=node
#             self.temp=node
#         else:
#             self.tail.next=node
#             self.tail=self.tail.next

#     def insert_begin(self,data):
#         node=Node(data)
#         node.next=self.head
#         self.head=node

#     def insert_end(self,data):
#         node=Node(data)
#         self.tail.next=node
#         node.prev=self.tail
#         self.tail=node

#     def print(self):
#         self.temp=self.head
#         while(self.temp):
#             print(self.temp.data)
#             self.temp=self.temp.next
# a=Circular_LinkedList()
# a.create(1)
# a.insert_begin(2)
# a.insert_end(3)
# a.print()

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def push(self,data):
#         node=Node(data)
#         if self.head==None:
#             self.head=node
#             self.tail=node
#         else:
#             node.next=self.head
#             self.head=node
#     def pop(self):
#         self.head=self.head.next
#     def peek(self):
#         print(self.head.data)
#     def Print(self):
#         self.temp=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
# a=stack()
# a.push(2)
# a.push(2)
# a.push(2)
# a.push(2)
# a.push(2)
# a.push(3)
# a.push(4)
# a.peek()
# a.pop()
# a.Print()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Queue:
#     def __init__(self):
#         self.front=None
#         self.rear=None

#     def Enqueue(self,data):
#         node =Node(data)
#         if self.front is None:
#             self.front=node
#             self.rear=node
#         else:
#             self.rear.next=node
#             self.rear=node
#     def Dequeue(self):
#         self.front=self.front.next

#     def print(self):
#         self.rear=self.front
#         while self.rear:
#             print(self.rear.data)
#             self.rear=self.rear.next
# a=Queue()
# a.Enqueue(1)
# a.Enqueue(2)
# a.Enqueue(3)
# a.print()

# from binarytree import bst
# root = bst(height=3, is_perfect=False)
# print("Binary Search Tree:")
# print(root)
# print("\nOperations:")
# print("Height:", root.height)
# print("Size:", root.size)
# print("Inorder Traversal:", list(root.inorder))
# print("Is BST:", root.is_bst)
# print("Min Value:", root.max_leaf_depth)
# print("Max Value:", root.min_leaf_depth)


# class Node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.Next=None
# class stack:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head=node
#             self.tail=node
#         else:
#             node.Next=self.head
#             self.head=node
#     def delete(self):
#         temp=self.head
#         self.head=self.head.Next
#         del temp

#     def print(self):
#         self.tail=self.head
#         while self.tail:
#             print(self.tail.data)
#             self.tail=self.tail.Next

# a=stack()
# a.create(1)
# a.create(12)
# a.delete()
# a.print()

# class Node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.Next=None
# class Queue:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head=node
#             self.tail=node
#         else:
#             self.tail.Next=node
#             self.tail=node
#     def get(self):
#         self.head=self.head.Next
    
#     def print(self):
#         self.tail=self.head
#         while self.tail:
#             print(self.tail.data)
#             self.tail=self.tail.Next

# a=Queue()
# a.create(1)
# a.create(11)
# a.get()
# a.print()




# class Node:
#     def _init_(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def _init_(self):
#         self.head=None
#         self.temp=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head=node
#             self.temp=node
#         else:
#             self.temp.next=node
#             self.temp=self.temp.next
#     def print(self,b,c):
#         self.temp=self.head
#         b=[]
#         c=[]
#         mid=len(a)//2
#         for j in range(0,len(a),2):
#             b.append(a[:mid])
#             break
#         for i in range(0,len(a),2):
#             c.append(a[mid:])
#             break
#         for i in range(len(b)):
#             print(*b[i])
#         for j in range(len(c)):
#             print(*c[j])
        

# sanj=LinkedList()
# a=int(input())
# l=list(map(int,input().split()))
# for i in l:
#     sanj.create(i)
# sanj.print()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.temp = None

#     def create(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#             self.temp = node
#         else:
#             self.temp.next = node
#             self.temp = self.temp.next

#     def print(self):
#         a = []
#         self.temp = self.head
#         while self.temp:
#             a.append(self.temp.data)
#             self.temp = self.temp.next

#         mid = len(a) // 2
#         b = a[:mid]
#         c = a[mid:]

#         for i in range(len(b)):
#             print(b[i], end=" ")
#         print()

#         for j in range(len(c)):
#             print(c[j], end=" ")
#         print()

# sanj = LinkedList()
# a = int(input())
# l = list(map(int, input().split()))
# for i in l:
#     sanj.create(i)
# sanj.print()


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.temp=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head=node
#             self.temp=node
#         else:
#             self.temp.next=node
#             self.temp=self.temp.next
#     def print(self):
#         self.temp=self.head
#         a=[]
#         while self.temp:
#             a.append(self.temp.data)
#             self.temp=self.temp.next

#         mid=len(a)//2
#         b=[]
#         c=[]
#         for i in range(len(a)):
#             b.append(a[i])
#         print(*b[:mid])
            
#         for j in range(len(a)):
#             c.append(a[j])
#         print(*c[mid:])

# a=LinkedList()
# l=list(map(int,input().split()))
# for i in l:
#     a.create(i)
# a.print()


# n=int(input())
# inner=[]
# for i in range(n):
#     outer=[]
#     for j in range(n):
#         n1=int(input())
#         outer.append(n1)
#     inner.append(outer)
# print(inner)
# n=int(input())
# inner=[]
# for i in range(n):
#     outer=[]
#     for j in range(n):
#         ni=int(input())
#         outer.append(ni)
#     inner.append(outer)
# print(inner)

# rathinam={}
# for i in range(3):
#     name=input()
#     age=int(input())
#     rathinam[name]=age
# print(rathinam)


# sanjay={}
# for i in  range(2):
#     a=int(input())
#     b=input()
#     sanjay[a]=b
# print(sanjay)

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.head=None
#         self.temp=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head=node
#             self.temp=node
#         else:
#             node.next=self.head
#             self.head=node
#     def delete(self):
#         self.head=self.head.next
#     def peek(self):
#         print(self.temp.data)
#     def print(self):
#         self.temp=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
# a=stack()
# a.create(1)
# a.create(2)
# a.create(3)
# a.delete()
# a.print()



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Queue:
#     def __init__(self):
#         self.head=None
#         self.temp=None
#     def Enqueue(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head=node
#             self.temp=node
#         else:
#             self.temp.next=node
#             self.temp=self.temp.next
#     def dequeue(self):
#         self.head=self.head.next
#     def print(self):
#         self.temp=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
# a=Queue()
# a.Enqueue(1)
# a.Enqueue(2)
# a.dequeue()
# a.print()


# class Node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.next=None
# class Queue:
#     def __init__(self) -> None:
#         self.head=None
#         self.temp=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head=node
#             self.temp=node
#         else:
#             self.temp.next=node
#             self.temp=self.temp.next
#     def delete(self):
#         self.head=self.head.next
#     def print(self):
#         self.temp=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
# a=Queue()
# a.create(1)
# a.create(2)
# a.delete()
# a.print()

# from pptx import Presentation

# # Create a presentation object
# prs = Presentation()

# # Slide 1: Title slide
# slide_1 = prs.slides.add_slide(prs.slide_layouts[0])
# title = slide_1.shapes.title
# subtitle = slide_1.placeholders[1]

# title.text = "Electrical Bulb Seminar"
# subtitle.text = "The Evolution of the Electrical Bulb"

# # Slide 2: Introduction
# slide_2 = prs.slides.add_slide(prs.slide_layouts[1])
# title, content = slide_2.shapes.title, slide_2.placeholders[1]
# title.text = "Introduction"
# content.text = "This seminar will explore the history and advancements in electrical bulbs."

# # Slide 3: Thomas Edison and the Incandescent Bulb
# slide_3 = prs.slides.add_slide(prs.slide_layouts[1])
# title, content = slide_3.shapes.title, slide_3.placeholders[1]
# title.text = "Thomas Edison and the Incandescent Bulb"
# content.text = "Thomas Edison's contributions to the development of the incandescent bulb."

# # Slide 4: Modern Innovations
# slide_4 = prs.slides.add_slide(prs.slide_layouts[1])
# title, content = slide_4.shapes.title, slide_4.placeholders[1]
# title.text = "Modern Innovations"
# content.text = "Advancements beyond incandescent bulbs: fluorescent, LED, and smart bulbs."
# # Save the presentation as a .ppt file
# prs.save("Electrical_Bulb_Seminar.ppt")


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.temp = None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head = node
#             self.temp=node
#         else:
#             self.temp.next=node
#             self.temp=self.temp.next
#     def print(self):
#         self.temp=self.head
#         self.temp1=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
#             self.temp

        

# sanj = LinkedList()
# l = list(map(int,input().split()))
# for i in l:
#     sanj.create(i)
# sanj.print(id(sanj))


# a=  [10,14,12,13,20,14]
# for i in range(len(a)+1):
#     print(id(i))

# a=[1]
# b=[34,21,324,34,67]
# c=a+b
# print(c)
# median=len(c)//2
# print(c[median])



# class Node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.next=None
# class Stack:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head=node
#             self.tail=node
#         else:
#             # node.next=self.head
#            node.next=self.head
#            self.head=node
#     def delete(self):
#         self.head=self.head.next
#     def print(self):
#         self.tail=self.head
#         while self.tail:
#             print(*self.tail.data,end=" ")
#             self.tail=self.tail.next
#         #         recursion()
#         # self.tail=self.head
#         # recursion()
# a=Stack()
# n=int(input("Enter the length of the Number:"))
# for i in range(n):
#     l=list(map(int,input().split()))
#     a.create(l)
# a.print()


# class List:
#     def __init__(self):
#         self.list=[]
#         self.count=0
#     def head_back(self,list):
#         self.list.append(list)
#         self.count+=1
#     def head_pop(self):
#         self.list.pop()
#         self.count-=1
#     def pop(self):
#         self.list.pop(0)
#         self.count-=1
#     def head_front(self,list):
#         self.list.insert(0,list)
#     def print(self):
#         print(self.list)


# a=List()
# a.head_front(2)
# a.head_back(5)
# a.head_front(1)
# a.pop()
# # a.head_pop()
# a.print()


# a=[1,2,3,4]
# for i in range(4-1):
#     a[i]=a[i]|[i+1]
# print(a)


# from itertools import combinations
# def AllPossibleStrings(self, s):
#     ans=[]
#     for i in range(1,len(s)+1):
#         comb=combinations(s,i)
#         for j in comb:
#             ans.append("".join(j))
#     return sorted(ans)





# from itertools import permutations
# a=[1,3,5]
# b=[]
# c=permutations(a,2)
# for i in c:
#     b.append(i)
# print(len(b))

# a="qwertyuioplkjhgfdsazxcvbnm"
# b="qwertyuiopasdfghjklzxcvbnm"
# c=a.lower()
# if c[-26:]==b:
#     print("Panagram")
# else:
#     print("Not Panagram")


# a=[10,10]
# c1=[]
# for i in range(0,2):
#      for j in range(i+1,2):
#         c1.append(a[i]-a[j])
# c1.sort(reverse=True)
# print(abs(c1[0]))

# s="z"
# a = list('abcdefghijklmnopqrstuvwxyz')
# s = s.lower()
# s = sorted(list(set(s)))
# if s[-26:] == a:
#     print("True")  
# else:
#     print("False")

# from itertools import combinations
# a="gfg"
# d=[]
# for i in range(1,len(a)+1):
#     c=combinations(a,i)
#     for j in c:
#         d.append("".join(j))
# print(*d)


# from itertools import combinations
# a="abc"
# c1=[]
# for i in range(1,len(a)+1):
#     c=combinations(a,i)
#     for j in c:
#         c1.append("".join(j))
# print(*sorted(c1))

# arr=[1,3,5]
# ans=0
# for i in range(len(arr)):
#     ones, zeros = 0, 0
#     for e in arr:
#         if e&(1<<i) == 0:
#             zeros += 1
#         else:
#             ones += 1
#     ans += zeros*ones*2
# print(ans)


# list=[25,77,54,81,48,34]
# count=0
# for i in list:
#     if i**0.5==int(i**0.5):
#         count+=1
# print(count)

# a=["4","43","345","20","987"]
# for i in a:
#     if len(i)>1:
#         tot=0
#         for j in range(len(i)):
#             tot+=int(i[j])
#         print(tot,end=" ")


# a=9
# print("%.9f" %float(a))

# print("\U000f1309")

# a=[1,2,3,4]
# c=[]
# # for i in range(len(a)-1):
# #     for j in range(i+1):
# #         if a[i]<a[i+1]:
# #             c.append(i)
# # print(c)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail=self.tail.next
    
#     def rotate(self, rot):
#         li=[]
#         for i in range(rot):
#             # self.tail.next = self.head
#             # self.tail = self.head
#             # self.head = self.head.next
#             # self.tail.next = None
#             li.append(self.head)
#             self.head = self.head.next
#         for j in li:
#             j.next=self.head
#             self.head = j

#     def print(self):
#         self.temp=self.head
#         while self.temp:
#            print(self.temp.data,end=" ")
#            self.temp=self.temp.next

# a=linkedlist()
# l=list(map(int,input().split()))
# for i in l:
#     a.create(i)
# a.rotate(2)
# a.print()



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail=self.tail.next
#     def even_rotate(self,l):
#         li=[]
#         ci=[]
#         c=[]
#         self.tail=self.head
#         for i in range(len(l)):
#             if l[i]%2 == 0:
#                 li.append(l[i])
                
#             else:
#                 ci.append(l[i])
#         li.reverse()
#         li.append(0)

#         for j in range(len(li)):
#             c.append(ci[j])
#             c.append(li[j])
#         c.pop()
#         print(*c)

#     def print(self):
#         self.tail=self.head
#         while self.tail:
#            print(self.tail.data,end=" ")
#            self.tail=self.tail.next

# a=linkedlist()
# l=list(map(int,input().split()))
# for i in l:
#     a.create(i)
# a.even_rotate(l)
# a.print()





# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail=self.tail.next
#     def swap(self,rotate):
#         for i in range(rotate):
#             self.tail.next=self.head
#             self.tail=self.head
#             self.head=self.head.next
#             self.tail.next=None
        
#     def print(self):
#         self.tail=self.head
#         while self.tail:
#            print(self.tail.data,end=" ")
#            self.tail=self.tail.next

# a=linkedlist()
# l=list(map(int,input().split()))
# rotate=int(input())
# for i in l:
#     a.create(i)
# a.swap(rotate)
# a.print()


# str = input('Enter a string : ')
# c = 0
# for i in str:
#     if not (ord(i) == 32 or 47<ord(i)<58 or 64<ord(i)<91 or 96<ord(i)<123):
#         c = c + 1
# print(c)

# a=int(input("Enter the factorial"))
# fact=1
# c=0
# for i in range(2,a):
#     fact=fact*i
#     print(fact)
# str_fact=str(fact)
# str_fact=str_fact[::-1]
# for i in str_fact:
#     if i=="0":
#         c=c+1
#     else:
#         break
# print(c)

'''
n = 2
a[] = {1, 10}
Output:
1
Explanation:
a[0] < a[1] so (j-i) is 1-0 = 1.'''

# a="sanjay"
# b="aeiou"
# c=sum(a.count(i) for i in b)
# print(c)


# n=int(input())
# if n<2:
#     print("Not a Prime")
# elif n==2:
#     print("Prime Number")
# else:
#     b=True
#     for i in range(2,int(n**5)+1):
#         if n%i==0:
#           b=False
#           break
# if b:
#     print("Prime")
# else:
#     print("None")


'''n = int(input())

if n < 2:
    print("Not a Prime")
elif n == 2:
    print("Prime Number")
else:
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Not a Prime Number")
    else:
        print("Prime")'''




# max_diff = 0

# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] < a[j] and j - i > max_diff:
#             max_diff = j - i

# print(max_diff)




# arr=["3", "30", "34", "5", "9"]
# A = sorted(arr,key=lambda x:str(x)*10,reverse=True)
# print("".join(A))
# print(A)


# b=[]
# e=[]
# for i in range(len(a)):
#     if a.count(a[i])>=3:
#         b.append(a[i])
#     else:
#         e.append(a[i])
# print(len(b))
# print(len(e))

# text="geeksforgeeks"
# pattern="geeks"
# l=[]
# for i in range(len(text)-len(pattern)+1):
#     if(text[i:i+len(pattern)])==pattern:
#         l.append(i+1)
# print(l)

# a=["12","34","45",'9','90']
# a1=sorted(a,key=lambda x:str(x)*10,reverse=True)
# print(a1)

# text="sanjay is a bad Boy"
# first='is'
# second="bad"
# a=text.index(first)
# b=text.index(second)



# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# c=0
# for i,j in statuses.items():
#     if j=="online":
#         c+=1
# print(c)


# a="TEsT"
# c=[]
# for i,j in enumerate(a):
#     if j.isupper():
#         c.append(i)
# print(c)

# a="ac"
# mid=len(a)//2
# odd=mid%2!=0
# if len(a)==2:
#     print(",")
# elif mid==odd:
#     print(a[mid])
# else:
#     print("")


# import random
# def random1():
#     a=random.randint(1,100)
#     return a



# def only_ints(a,b):
#     f=str(a)
#     c=str(b)
#     if f=='-1':
#         return True
#     elif f.isdigit() and c.isdigit():
#         return True
#     else:
#         return False    
# a=-1
# b=999
# print(only_ints(a,b))

# def anagram(a,b):
#     if sorted(a)==sorted(b):
#         return True
#     else:
#         return False
# a="typhoon"
# b="opython"
# print(anagram(a,b))

# def div_3(a):
#     if a==1 or a==3:
#         return True
#     elif a//3==0:
#         return True
#     else:
#         return False
# a=1
# print(div_3(a))

# a=[6,4,2,1,5]
# for i in range(len(a)):
#     c=0
#     for j in range(i+1,len(a)):  
#         if a[i]>a[j]:
#             c+=1
#     print(c,end=" ")

# for row in range(5):
#     for col in range(5):
#         if row==0 or col==2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()



# a=[2,1,5,6,4]
# sort=sorted(a)
# c=0
# front=sorted(a[:mid])
# end=sorted(a[mid:])
# sd=front+end
# for i in range(len(a)):
#     if (sd==sort):
#         c+=1
#     else:
#         break
# print(c,end=" ")
# c=[]
# d=[]
# for i in range(len(a)-1,2):
#     mid=len(a)//2
#     if a[i]>a[i+1]:
#         c.append(a[i])
#         c.append(a[i+1]) 
#     else:
#         d.append(i)    
# print(c,d)

# n = 7
# l = [2,1,5,6,4]
# c = 0
# i = 0
# k = n
# while k > 1:
#     f = 0
#     for j in range(i+1,n):
#         if l[j] < l[i]:
#             s = j
#             f = 1
#     c = c + 1
#     if f == 1:
#         i = s + 1
#         k = k - s
#     else:
#         i = i + 1
#         k = k - 1
# print(c)



# def longestSubstring(s):
#     longest_substring = ""
#     for i in range(len(s)):
#         for j in range(i + 1, len(s) + 1):
#             substring = s[i:j]
#             if s.count(substring) > 1 and len(substring) > len(longest_substring):
#                 longest_substring = substring

#     return longest_substring
# s="sanjayumarsanjay"
# print(longestSubstring(s))


# class Node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.next=None
# class Linked_List:
#     def __init__(self):
#         self.head=None
#         self.temp=None
#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head=node
#             self.temp=node
#         else:
#             self.temp.next=node
#             self.temp=self.temp.next
#     def print(self):
#         self.temp=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
# a=Linked_List()
# a.create(1)
# a.create(1)
# a.create(2)
# a.print()   

# s="sa1njay umar sa1njay"
# b="sa1njay"
# print(s.count(b))

# s="sanjayumarsanjay"
# l=""
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         substring=s[i:j]
#         if s.count(substring)>1 and len(substring)>len (l):
#             l=substring
# print(l)



# a="qw@78#fe1"
# only_alphabet=""
# output=""
# for j in a:
#     for i in j:
#         if i.isalnum():
#             only_alphabet+=i
#         else:
#             output+=only_alphabet[::-1]+i
#             only_alphabet=""
# print(output)
# print(only_alphabet)



# a="qwert%$#"
# string=""
# special=""
# for i in a:
#     for j in i:
#         if j.isalnum():
#             string+=j
#         else:
#             special+=string[::-1]+j
#             string=""
# print(special)


# a="5783789"
# A=sorted(a, key=lambda x:str(x)*10,reverse=True)
# print("".join(A))

# def reverse(a):
#     b=[]
#     for i in str(a):
#         b.append(i)
#     return "".join(b[::-1])
# a=578


# def reveersse(a):
#     c=[]
#     for i in range(len(a)-1,-1,-1):
#         c.append(a[i])
#     return c

# a=list(map(str,input().split()))
# print(reveersse("".join(*a)))

# a=int(input("Enter the Value:"))
# r=0
# while a!=0:
#     r=(r*10)+(a%10)
#     a=int(a/10)
# print(r)


#     l.append(r)
#     a=a//2
# l.reverse()
# for ele in l:
#     print(ele,end='')

'''
a=[29,38,12,48,39,55]
c=[]
for i in range(len(a)):
    if a[i]>30 and a[i]<50:
        print(i,end="")'''
        # c.append(a.index(a[i]))
# print(*c)


# class Node:
#     def __init__(self,data) -> None:
#         self.data=data
#         self.next=None
#         self.prev=None
# class lnked:
#     def __init__(self):
#         self.head=None
#         self.temp=None

#     def create(self,data):
#         node=Node(data)
#         if self.head is None:
#             self.head=node
#             self.temp=node
#         else:
#             self.temp.next=node
#             node.prev=self.temp
#             self.temp=node
#     def print(self):
#         self.temp=self.head
#         while self.temp:
#             print(self.temp.data)
#             self.temp=self.temp.next
# s=lnked()
# s.create(1)
# s.create(2)
# s.create(3)
# s.print()


# a=[1,2,3,4,6]
# v=list(filter(lambda x :(x%2==0),a))
# print(v)

# for i in [1,2,3,4,5]:
#     for j in range(len(i)):
#         print("*",end="")

# a=[[1,2,3],
#    [4,5,6],
#    [7,8,1]]
# a1=[[1,2,3],
#    [4,5,6],
#    [7,8,20]]
# for i in range(len(a)):
#     c=[]
#     for j in range(len(a1)):
#         # c.append(a[i][j]+a1[i][j])
#         if a[i][j]+a1[i][j]==21:
#             c.append(a[i])
#     print(c)

# mat1 = [[1, 2],
#         [3, 4]]
# mat2 = [[4, 5],
#         [6, 7]]
# for i in range(len(mat1)):
#     c = []
#     for j in range(len(mat1[0])):
#         for k in range(len(mat2)):
#             for l in range(len(mat2[0])):
#                 if mat1[i][j] + mat2[k][l] == 10:
#                     c.append((mat1[i][j], mat2[k][l]))
# print(len(c))
# print("Pairs whose sum found to be 10 are:", c)

# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# for i in range(len(a)):
#     if i%2==0:
#         print(*a[i],end=" ")
#     else:
#         print(*a[i][::-1],end=" ")

'''a='abcdcdc'
b='cdc'
c=0
d=len(b)
for i in range(len(a)-len(b)+1):
    if a[i:d+i]==b:
        c+=1
print(c)'''


'''a1= [11, 7, 1, 13, 21, 3, 7, 3]
a2 = [11, 3, 7, 1, 7]
a=[]
b=True
for i in a2:
    if i not in a1:
        b=False
if b:print("Yes")
else:print("No")'''

'''def s(a):
    c=[]
    for i in range(0,max(a)):
        c.append(i)
    return sorted(str(c[-1]))[0]
   
a=[1,3,2,4,6,8,5]
print(s(a))'''

# a=[1,2,3,4,5]
# b=4
# c=0
# while a:
#     mid=len(a)//2
#     if b==a[mid]:
#         print(a[mid])
#         c=1
#         break
#     elif b<a[mid]:
#         a=a[:mid]
#     elif b>a[mid]:
#         a=a[mid+1:]

# if c==1:
#     print("Found")
# else:
#     print("Not Found")

# a=[[1,7,2],
#    [3,4,5],
#    [4,2,1]]
# for i in range(len(a)):
#     if i%2==0:
#         print(*a[i],end=" ")
#     else:
#         print(*a[i][::-1],end=" ")


# n=3
# a=0
# b=1
# c=0
# c1=[]
# for i in range(n):
#     c=a+b
#     b=a
#     a=c
#     c1.append(c)
# # g(3) = 3*g(2) + 3*g(1) + 3 = 3*1 + 3*1 + 3 = 9
# g_F=n*c1[0]+n*c1[1]+n
# print(g_F%5)


# a=[1,2,3,-1]
# current=a[0]
# sum=0
# for i in a:
#     current1=max(i,sum+i)
#     sum=max(sum,current1)
# print(sum)


# a1="cat latt batman superman latt cat"
# a=a1.split()
# n=0
# c=[]
# for i in a:
#     if a.count(i)==n and i not in c:
#         c.append(i)
#     else:
#         print("NA")
#         break
# print(*c)


# input="aaaabbcccn"
# c=''
# for i in input:
#     if i not in c:
#         c+=i
# for i in c:
#     v=input.count(i)
#     print("".join((f'{v}',i)),end="")


# input1=["a","b","name"]
# input2=["1","2","prakesh"]
# x=dict(zip(input1,input2))
# print(x)


# a=[["Jay",80],["viru",85],["sanjay",90],["leo",45],]
# value=[]
# for i,j in a:
#     value.append(j)
# x=sorted(value,reverse=True)
# second=x[1]
# for i,j in a:
#     if j==second:
#         print(i)


''''a=[1,2,3,-1,-2,67]
c=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==0:
            c+=1
print(c)'''


'''a=[1,2,3,6,8]
if a==sorted(a):
    print("True")
else:
    print("False")'''

# a=[1,2,3,1,3,5]
# b=a
# c=[]
# dict={}
# for i in b:
#     dict[i]=a.count(i)
# for i,j in dict.items():
#     if j ==2:
#         c.append(i)
# print(c)

# l=["7 student","14 sy","5 mi"]
# b=[]
# for i in l:
#     j=i.split()
#     for f in j:
#         if f.isdigit():
#             b.append(f)
# print(b)

n=int(input("Enter the Tables:"))
for i in range(0,11):
    print(f"5*{i}=",n*i)