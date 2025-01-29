string=input("enter the string:-")
length=len(string)
parts=int(length/3)

# print("left sub string",string[0:parts])
# print("middle sub string",string[parts:length-parts])
# print("right sub string",string[length-parts:length])
print("left sub string ")
for i in range(0,parts):
    print(string[i],end="")

# for i in range(parts,length-parts):
#     print("middle sub string",string[i],end="")

# for i in range(length-parts,length):
#     print("right sub string",string[i],end="")





