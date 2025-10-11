#dictionnary struce 
person = {"name" : "Oussama", "surname" : "IG", "age" : 24}

#to dict
colors = [("red", "#f00"), ("green", "#0f0"), ("black", "#000"), ("white", "#fff")]
colors_dict = dict(colors)

#insert a new value
person["occupation"] = "Entrepreneur"

#update a value
person["age"] = 25

#access a value : dictName[key]
print(person["name"])

#membership
if "number" in person:
    person["number"] = 27
else:
    print("invalud key")

#length
print(len(person))

#how to delete an element(key, value) : del dictName[key]
del person["occupation"]

#popitem() : delete and return the last element as tuple
key, val = person.popitem()

#delete dictionary
person.clear()


mydict = {"ID194646": 15, "ID64646446" : 18, "ID65656565": 12, "ID642125": 14,"ID65758626565": 17,"ID6561445565": 19}

#dictionary keys to list
list_keys = list(mydict.keys())
print(list_keys)
#dictionary values to list
list_values = list(mydict.values())
print(list_values)

#dictionary values to set
set_values = set(mydict.values())
print(set_values)

#dictionary to tuple
items_tuple = tuple(mydict.items())
print(items_tuple)

#lists to dictionary
mydict2 = dict(zip(list_keys, list_values))
print(mydict2)

#list to dictionary manually
dict2 = {}
for i in range(len(list_keys)):
    dict2[list_keys[i]] = list_values[i]
print(dict2)