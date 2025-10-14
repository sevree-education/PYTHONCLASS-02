filename = "./CLASS 10/students.csv"#
mode = "r"

filecontent = []

with open(filename, mode) as f:
    for line in f:
        line_list = line.strip().split(",")
        filecontent.append(line_list)

with open(filename, mode) as f:
    lines = f.readlines()

print(filecontent)
print(lines)