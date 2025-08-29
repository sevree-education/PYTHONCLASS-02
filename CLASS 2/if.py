a = int(input("Give A : "))
b = int(input("Give B : "))

#how to define a condition
if (a > b):
    print(f"The value of (A : {a}) is bigger than the value of (B : {b})")

#how to define an else if
elif (b > a):
    print(f"The value of (B : {b}) is bigger than the value of (A : {a})")

#how to define else
else:
    print(f"(A : {a}) is equal to (B : {b})")
