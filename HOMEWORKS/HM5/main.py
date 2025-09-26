from fact import *
from prime import *
n = int(input("GIVE ME AN N : "))
factN = Fact(n)

primesTotal = 0
for i in range(1, factN+1):
    if IsPrime(i):
        primesTotal = primesTotal + i

print(f"THE SUM OF PRIME NUMBERS BETWEEN 1 AND THE FACT OF {n} WHICH IS {factN} IS {primesTotal}")
