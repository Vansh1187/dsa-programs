def push(stack,element):
    stack.append (element)
    print("Element is inserted")
def pop(stack):
    if len(stack)==0:
        print("stack is empty")
    else:
        print("Element removed",stack.pop())
def peek(stack):
    if len(stack)==0:
        print("stack is empty")
    else:
        i=len(stack)-1
        print ("The topmost element is",stack[i])
def display(stack):
     if len(stack)==0:
        print("stack is empty")
     else:
        for i in range(len(stack)-1,-1,-1):           
            print(stack[i])
stack=[]
maxsize=int(input("Enter the size of array"))
while True:
    i=int(input("Enter a number 1.push 2.pop() 3.peek() 4. display()"))
    if i==1:
        if len(stack)>=maxsize:

            print("stack is overflow")
        else:
            element=input("Enter a number to insert")
            push(stack,element)
    elif i==2:
        if len(stack)<1:
            print("stack is underflow")
        else:
            pop(stack)
    elif i==3:
        peek(stack)
    elif i==4:
        display(stack)
    else:
        print("Invalid response")
        break
if len(stack)<=0:
    print("stack is empty")
else:
    print("The final stack is")
    for i in range(0,len(stack)):
        print(stack[i])
    



