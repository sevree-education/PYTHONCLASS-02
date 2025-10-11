from functions import *
while True:
    print("CALCULATOR HOME SCREEN")
    menu()
    choice = input("CHOOSE OPERATION : ")
    if choice == "q":
        print("GOOD BYE")
        break
    elif choice == "1":
        a, b = getinput()
        print(add(a,b))
        print("\n")
    elif choice == "2":
        a, b = getinput()
        print(sub(a,b))
        print("\n")
    elif choice == "3":
        a,b = getinput()
        print(multi(a,b))
        print("\n")

    elif choice == "4":
        a,b = getinput
        print(mod(a,b))
        print("\n")
    elif choice == "5":
        a,b = getinput()
        r = div(a,b)
        print(f"THE RESULT IS {r:.2f}")
        print("\n")
    elif choice == "6":
        a,b = getinput()
        print(pow(a,b))
        print("\n")
    elif choice == "7":
        a = int(input("give value of a : "))
        print(mysin(a))
        print("\n")
    elif choice == "8":
        a = int(input("give value of a : "))
        print(sqrt(a))
        print("\n")
    elif choice == "9":
        a,b = getinput()
        print(andOp(a,b))
        print("\n")
    elif choice == "10":
        a,b = getinput()
        print(orOp(a,b))
        print("\n")
    else:
        print("INVALID OPERATION")



