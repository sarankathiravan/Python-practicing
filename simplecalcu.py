a=int(input("Enter value for A"))
b=int(input("Enter value for B"))
mode=input("OPERATION TO PERFORM: ")
if(mode=="add"):
    print("The sum of A and B is: ",a+b)
elif(mode=="sub"):
    print("The difference of A and B is: ",a-b)
elif(mode=="mul"):
    print("The multiplication  of A and B is: ",a*b)
elif(mode=="div"):
    print("The division of A and B is: ",a/b)
else:
    print("Invalid input")      