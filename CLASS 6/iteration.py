#direct item iteration:
mylist = [10, 50, "Oussama", 11, "123213", 15, "laksdas", 11]
for element in mylist:
    print(element)

print("\n")
#Index Loop
for i in range(len(mylist)):
    print(mylist[i])

print("\n")
#enumerate()
for index, value in enumerate(mylist, start=0):
    print(f"The value at index {index} is {value}")

print("\n")
#WHILE()
index = 0
while index < len(mylist):
    print(mylist[index])
    index+=1