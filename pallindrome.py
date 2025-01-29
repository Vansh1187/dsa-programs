# string=input("enter the string value:")
# reversed_string=string[::-1]
# if(string==reversed_string):
#     print("pallindrome")
# else:
#     print("not pallindrome")

# without slice

# string=input("enter the string value:")
# reversed_string=""
# a =len(string)-1
# while(a>-1):
#     reversed_string=reversed_string+string[a]
#     a-=1
# if string==reversed_string:
#     print("pallindrome")
# else:
#     print("not pallindrome")

# with double pointer

string=input("enter the string value:")
reversed_string=""
i=0
for k in range(len(string)-1,-1,-1):
    if(string[i]==string[k]):
            if(i==k or i==k+1):
                print("pallindrome")
                break
    
    else:
        print("not pallindrome")
        break
    i+=1





