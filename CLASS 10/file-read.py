filename = "./CLASS 10/data.txt"
mode = "r"

#open file with context manager:
with open(filename, mode) as f:
    #read the entire content at once
    filecontent = f.read()

#read file content line by line
with open(filename, mode) as f:
    line1 = f.readline()
    line2 = f.readline()

#read file line by line and return it in a list
with open(filename, mode) as f:
    lines = f.readlines()

#iterate through the whole file
with open(filename, mode) as f:
    for line in f:
        print(line.strip())