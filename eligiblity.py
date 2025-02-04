salary=int(input("Enter your salary: "))
age=int(input("Enter your age: "))
if(salary>=25000 or age>=35):
    loan_amount=int(input("Enter loan amount: "))
    if(loan_amount<50000):
        print("you are eligible for loan")
    else:
        print("amount is beyond the limit")
else:
    print("you are not eligible")