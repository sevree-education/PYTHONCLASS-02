vowels = "aeuoiy"

user_string = str(input("What do you want to say : ")).lower()

sum = 0

for x in user_string:
    if x in vowels :
        sum += 1

print(sum)