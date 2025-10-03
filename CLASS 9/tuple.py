#how to define a tuple
gpscoords = (41.008, 28.456)
point = (4, 8)
point3d = (12, 9, 120)

#unpacking
x, y, z = point3d

#define a tuple from string
name = "OUSSAMA"
mytup = tuple(name)

#size of a tuple
sizeoftuple = len(mytup)

#contains
if "O" in mytup:
    print("Exists")

#indexing
firstelement = mytup[0]

#iteration
for element in mytup:
    print(element)

#tuple to list:
infos = ("OUSSAMA", "IG", 24)
newlist = list(infos)

list = ["OUSSAMA", "SOFIANE", "HICHEM"]
studentstuple = tuple(list)