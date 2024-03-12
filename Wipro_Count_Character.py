def count_word_in_str(a1,n):
    a=a1.split()
    c=[]
    for i in a:
        if a.count(i)==n and i not in c:
            c.append(i)
        if not c:
            print("NA") 
            break
    print(*c)
a=str(input("Enter the Word:"))
n=int(input("Please Enter the Input Count:"))
count_word_in_str(a,n)
