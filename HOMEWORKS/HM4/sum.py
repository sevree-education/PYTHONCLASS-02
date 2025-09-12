try:
    n = int(input("Please give me a number : "))
except Exception as e:
    print(e)

sum = 0

for x in range(1, n+1):
    sum = sum + x

print(sum)