def Common_letter(str1,str2):
    output=''
    for i in str1:
        if i in str2:
            output += i
    return output

str1=input("Please Enter String 1:")
str2=input("Please Enter String 2:")
print(Common_letter(str1,str2))