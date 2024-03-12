a1="123python456"
string=""
alpha=""
for i in a1:
    for j in i:
        if i.isdigit():
            string+=i
        else:
            alpha+=i
print(string)
print(alpha)