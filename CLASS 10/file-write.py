filename = "./CLASS 10/mydata.txt"
file2 = "./CLASS 10/data.txt"
#we have two modes
# w : write (create or truncate an existing file)
# a : append (create if missing, then add to the end)
mode = "w"

with open(filename, mode) as f:
    #to write in a file
    f.write("FIRST IS THE FIRST LINE\n")
    f.write("SECOND LINE")

#writing multiple lines from a list
lines= ["OUSSAMA\n", "IG\n", "SEVREE EDUCATION\n", "5122022\n"]
with open(filename, mode) as f:
    f.writelines(lines)

#appending not overwriting
with open(file2, "a") as f:
    f.write("\nTHIRD LINE")
    

