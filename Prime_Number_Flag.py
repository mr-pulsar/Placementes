input=int(input("Please Enter The Value:"))
if input<2:
    print("Not a Prime Number")
elif input==2:
    print("Prime Number")
else:
    Flag=True
    for i in range(2,int(input**0.5)+1):
        if input%i == 0:
            Flag=False
    if Flag:print("Prime")
    else:print("Not a Prime")