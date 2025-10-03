myfullname  = "     OUSSAMA IG     "

#strip() : delete all spacing around the string
print(myfullname)
print(myfullname.strip())

#lower() : returns a lowercase version of your string
print(myfullname)
print(myfullname.lower())

#upper() : return a uppercase version of your string
lowername = myfullname.lower()
print(lowername)
print(lowername.upper())

#combine both functions
print(lowername.strip().lower())

#split(x) : breaks the string a x and returns a list
mystring = "HELLO IM OUSSAMA IG"
words = mystring.split()
print(words)

#join(x) : join the elements of a list using x
newstring = ", ".join(words)
print(newstring)

#fString
name = "Oussama"
age = 24

print(f"My name is {name} and i am {age}yo")

randomnumber = 2.164764641631
print(f"your name is {randomnumber:.5f}")