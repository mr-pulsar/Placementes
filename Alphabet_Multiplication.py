'''Method 1'''
# a="a2b3c6"
# alpha=''
# for i in a:
#     if i.isalpha():
#         alpha+=i
#     else:
#         c=alpha*int(i)
#         print(c,end="")
#         alpha=""



'''Metod 2'''
a="a2b3c4"
alpha=''
num=''
for i in a:
    if i.isalpha():
        alpha+=i
    else:
        num+=i
print(alpha)
print(num)
for i,j in zip(alpha,num):
    print(i*int(j),end="")