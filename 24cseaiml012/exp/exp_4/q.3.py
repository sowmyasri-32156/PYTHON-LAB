a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
gcd=1
i=1
while (i<a and i<=b and i<=c):
    if(a%i==0 and b%i==0 and c%i==0):
        gcd=i
        i=i+1
        print("gcd of three numbers:",gcd)        
