string=input("enter the sentence.-")
l=string.split(" ")
largest_word=""
largest_length=0
for i in l:
    length=len(i)
    if length>largest_length:
        largest_word=i
        largest_length=length
print("largest word in the sentence is- ",largest_word)

