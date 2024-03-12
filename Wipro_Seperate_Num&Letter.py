def Sep_Num_Letter(a):
    number=''
    alpha=''
    for i in a:
        if i.isalpha():
            alpha+=i
        else:
            number+=i
    v=sorted(alpha)+sorted(number)
    print("".join(v))
    
input=input("Please Enter the Word:")
Sep_Num_Letter(input)