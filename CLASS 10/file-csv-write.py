students = [
    ["OUSSAMA", "IG", "24"],
    ["SOFIANE", "XX", "20"],
    ["HICHEM", "YY", "19"]
]

#writing list to an csv file:
with open("./CLASS 10/students.csv", "w") as f:
    for student in students:
        line = ",".join(student) + "\n"
        f.write(line)

