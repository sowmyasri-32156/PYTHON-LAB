b=float(input("enter a number:"))
a=float(input("enter a number:"))
c=float(input("enter a number:"))
d=b*b - 4*a*c
if d > 0:
    r1=(-b + math.sqrt(d)/2*a)
    r2=(-b - math.sqrt(d)/2*a)
    print("two real roots: ", r1,r2)
elif d == 0: 
    r = -b/(2*a)
    print("one real root: ",r)
else:
    print("no real roots")