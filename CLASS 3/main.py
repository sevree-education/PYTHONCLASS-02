try:
    val1 = int(input("Give a value : "))
    val2 = int(input("Give a value : "))
    print("The result of the division is : ", val1/val2)
except ZeroDivisionError:
    print("You cannot divide by 0")
except ValueError:
    print("Please enter a correct value")

print("Rest of the code")