mylist = [10, 50, "Oussama", 11, "123213", 15, "laksdas", 11]

#append(x): add x to the end of the list
mylist.append(0)

#insert(i, x): puts x before the position i:
mylist.insert(2, 55)

#pop(): removes and returns the last element:
deletedvalue = mylist.pop()

#pop(i): removes and returns the item at index i:
deletedvalue = mylist.pop(1)

#remove(x): removes the first occurrence of the value x:
try:
    mylist.remove(178)
except Exception as e:
    print(e)

print(mylist)

#len(listname): returns number of elements in the list
print(len(mylist))