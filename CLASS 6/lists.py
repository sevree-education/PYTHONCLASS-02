#how to declare a list:
mylist = [10, 50, "Oussama", 11, "123213", 15, "laksdas"]

#how to print element after element (Parcours):
for element in mylist:
    print(element)

#access to one element:
print(mylist[2])
print(mylist[-2])

#change the value of an element:
mylist[0] = "new_element"

#how to changes all values of a list:
for i in range(len(mylist)):
    mylist[i] = 0
