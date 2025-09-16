mypassword = "admin123"
counter = 0

while True:
    user_pass = int(input("Enter your password : "))

    if(mypassword == user_pass):
        print("Valid password")
        break
    else:
        print("Password Invalid, please try again")
        counter = counter + 1

    if counter >= 3:
        break


while True:
    user_pass = str(input("Enter your password : "))

    if(mypassword == user_pass):
        print("Valid password")
        break
    else:
        print("Password Invalid, please try again")
        counter = counter + 1

    if counter >= 3:
        break