mylist = [10, 50, "Oussama", 11, "123213", 15, "laksdas"]

#to slice a list: 
#newlist = list[start : stop : step]
newlist = mylist[:2]
print(newlist)
newlist = mylist[2:]
print(newlist)
newlist = mylist[-2:]
print(newlist)
newlist = mylist[::3]
print(newlist)
newlist = mylist[::-1]
print(newlist)