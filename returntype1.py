U_name="SK"
P_word="123"
credential1=input("Username: ")
credential2=input("Password: ")
def validation(username,password):
    if(U_name==username and P_word== password):
        return True
    else:
        return False
validation(credential1,credential2)
print(validation(credential1,credential2))