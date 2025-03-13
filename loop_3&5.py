count_3=0
count_5=0
for i in range (1,101):
    if(i%3==0):
        print("The number ",i," is divisable by 3")
        count_3=count_3+1
    elif(i%5==0):
        print("the number ",i," is divisable by 5")
        count_5=count_5+1
print("Total no of numbers divide by 3 between 1 to 100 is : ",count_3)
print("Total no of numbers divide by 5 between 1 to 100 is : ",count_5)


    