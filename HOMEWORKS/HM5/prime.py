from math import sqrt

def IsPrime(n):
    isprime = True
    i = 2
    if(n != 1 and n !=0):
        while isprime and i <= sqrt(n):
            if n % i == 0:
                isprime = False
            i+=1
        return isprime
    else:
        return False

