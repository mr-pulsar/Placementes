'''import random
player1=input('Enter Your Choice:')
player2=input('Enter Your Choice:')
length=1
a=''.join(random.sample(player1,length))
print('Player1 Has Entered:',player1)
b=''.join(random.sample(player2,length))
print('Player2 Has entered:',player2)

if player1==player2:
    print("Match tied")
elif player1>player2:
    print("Player1 Wins")
elif player1 == 'pencil' and player2 == 'paper':
    print("Player1 Wins")
elif player1 == 'paper' and player2 == 'pencil':
    print("Player2 Wins")
elif player1 == 'paper' and player2 == 'scissores':
    print("Player2 Wins")
elif player1 == 'scissores' and player2 == 'paper':
    print("Player1 Wins")
else:
    print("Player2 Wins")'''


'''board=[" "for i in range(9)]
row1="|{}|{}|{}|".format(board[0],board[1],board[2])
row2="|{}|{}|{}|".format(board[3],board[4],board[5])
row3="|{}|{}|{}|".format(board[6],board[7],board[8])
choice=input("Enter the Choice of Player1:")
for i in range(9):
    if choice=="x":
        pos=int(input('X position:'))
        if " " in board[pos]:
            board[pos]=choice
            choice="o"
        else:
            print("Input Wrong")
            break

    else:
        pos=int(input('O position:'))
        if " " in board[pos]:
            board[pos]=choice
            choice="x"
        else:
            print("Input Wrong")
            break
a="x"
b="o"
if board[0]==board[1]==board[2]==a or board[3]==board[4]==board[5]==a or board[6]==board[7]==board[8]==a or board[0]==board[3]==board[6]==a or board[1]==board[4]==board[7]==a or board[2]==board[5]==board[8]==a or board[0]==board[4]==board[8]==a or board[2]==board[4]==board[6]==a :
    print("A wins")
elif board[0]==board[1]==board[2]==b or board[3]==board[4]==board[5]==b or board[6]==board[7]==board[8]==b or board[0]==board[3]==board[6]==b or board[1]==board[4]==board[7]==b or board[2]==board[5]==board[8]==b or board[0]==board[4]==board[8]==b or board[2]==board[4]==board[6]==b :
    print("B wins")
else:
    print("Draw")

print(board[0],board[1],board[2])
print(board[3],board[4],board[5])
print(board[6],board[7],board[8])

import random
a=random.randint(0,20)
Initial_Score =100
Player1=int(input("Enter the Numbers:"))
if Player1==a:
    print(f"Player Wins Your Point is {Initial_Score}")
else:
    print("Wheather You Need Second Chance")
    Player1=str(input(("Yes or No:")))
    if Player1=="Yes":
        if a%2==0:
            print("Clue")
            print("My number is EvEn")
        else:
            print("Clue")
            print("My number is OdD")
        Player1=int(input("Enter The Second Chance:"))
        if Player1==a:
            print(f"{Initial_Score-50}")
        else:
            print("Failed")
            print("My Numbree is:",a)
    else:
        print("Thank You Come Again!")


import random
upper="WERTYUIOPASDFGHJKLZXCVBNM"
lower="qwertyuiopasdfghjklzxcvbnm"
symbol="!@#$%^&*()"
length=15
password=upper+lower+symbol
print("".join(random.sample(password,length)))


a="sanjay"
b=""
c=""
for i in a:
    if a.count(i)==2:
        c+=i
    else:
        b+=i
print(b)'''

'''b={'Alice':100,"Bob":99,"Kumar":76}
d=dict(sorted(b.items(),reverse=True))
print(d)

def insertion(arr):
    for i in range(len(arr)):
        b=i
        while b>0 and arr[b]<arr[b-1]:
            arr[b],arr[b-1]=arr[b-1],arr[b]
    return arr
arr=[4,3,1,5,7,8]
insertion(arr)
print(insertion(arr))'''

# import qrcode
# img=qrcode.make("www.google.com")
# img.save("sw.png")

'''def insertion (arr):
    for i in range(len(arr)):
        b=i
        while b>0 and arr[b]<arr[b-1]:
            arr[b],arr[b-1]=arr[b-1],arr[b]
    return arr
a=[32,12,43,545,231]
print(insertion(a))'''
                
a="sanjay"
b=["a","e","i","o","u"]
c1=0
for i in a:
    if i in b:
        c1+=1
print(c1) 

