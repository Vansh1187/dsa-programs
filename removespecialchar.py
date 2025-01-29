string=input("enter the string")
newString=""
for i in string:
    if((ord(i) in range(65,91))or(ord(i)in range(97,123))):
        newString=newString+i
print(newString)

