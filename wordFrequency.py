string=input("enter the string:- ")
l=string.split(" ")
d={}
for i in l:
    d[i]=string.count(i)
    
for i in d:
    print(i,d[i])

