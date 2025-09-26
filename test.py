n = int (input("Enter a number :"))
if n<0 :
    n=-n
if n==0 :
    print(0)

x = 1
while x*10 <=n :
    x=x*10
while x>0 : 
    d = n//x
    print(d)
    n = n % x
    x = x // 10 