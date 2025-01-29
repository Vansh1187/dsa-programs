string=input("Enter the string: ")
reversed_String=""
for i in range(len(string)-1,-1,-1):
    reversed_String=reversed_String+string[i]
print(reversed_String)