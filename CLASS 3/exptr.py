try:
    val1 = int(input("Give a value : "))
    val2 = int(input("Give a value : "))
    print("The result of the division is : ", val1/val2)
except Exception as e:
    print("An error has occurred, error type is :", e)

print("Rest of the code")