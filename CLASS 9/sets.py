#define a set
s = set()

#list to set
myset = set([1, 5, 3, 4 ,3,2])

#add an element
myset.add(0)

#remove an element
try:
    myset.remove(2)
except Exception as e:
    print(e)

myset.discard(465)

#remove last element added
x = myset.pop()

#clear
myset.clear()


group_a = {"Oussama", "Hichem", "Nacer"}
group_b = {"Ikram", "Sofian", "Lilya", "Oussama"}

#Union
allgroups = group_a | group_b

allgroups = group_a.union(group_b)

#intersection
inters = group_a & group_b
inters = group_a.intersection(group_b)

#difference
diffs = group_a - group_b
diffs = group_a.difference(group_b)
print(diffs)
