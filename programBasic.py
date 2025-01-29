# # Basic program-1
# a='welcome'
# for i in a:
#     if(i=='c'):
#         print("@@",end="")
#     print(i,end="")

# Basic program-2

String=input("enter a string:- ")
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0

for char in String:
    if char in vowels:
        vowel_count+=1
    else:
        consonant_count+=1
print("total vowel",vowel_count)
print("total consotant",consonant_count)

