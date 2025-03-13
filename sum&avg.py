A=[]
for i in range(1,11):
    num=int(input("Enter the number "+ str(i)+(":")))
    A.append(num)
print(A)
sum=0
for i in A:
    sum=sum+i
print(sum)