val1 = int(input("GIVE A VALUE : "))
val2 = int(input("GIVE A VALUE : "))
val3 = int(input("GIVE A VALUE : "))

if(val1 > val2):
    max = val1
    min = val2
else:
    max = val2
    min = val1

if(val3 > max):
    max = val3
else:
    min = val3

print(f"The highest values is {max} and the lowest is {min}")