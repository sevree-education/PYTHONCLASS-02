import math
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def mod(a,b):
    return a % b

def div(a,b):
    if b != 0:
        return a / b
    else: 
        return None
    
def sqrt(a):
    return math.sqrt(a)

def pow(a,b):
    r = 1
    for i in range(b):
        r = r * a
    return r

def mysin(a):
    return math.sin(a)

def andOp(a,b):
    return a and b

def orOp(a,b):
    return a or b


def menu():
    print("DECIMAL OPERATION:")
    print("1-ADD")
    print("2-SUB")
    print("3-MULT")
    print("4-MOD")
    print("5-DIV")
    print("6-POW")
    print("7-SIN")
    print("8-SQRT")
    print("---------------------------------------------------\n")
    print("BINARY OPERATION:")
    print("9-AND")
    print("10-OR")
    print("---------------------------------------------------\n")
    print("q : TO QUIT")


def getinput():
    a = int(input("give value of a : "))
    b = int(input("give value of b : "))
    return(a,b)



def myfunction(*args, **kwargs):
    print("element", args)
    print("keys", kwargs)
