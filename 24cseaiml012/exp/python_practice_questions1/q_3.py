def natural(n):
    if n<=0:
        return "please enter a positive number"
    elif n==1:
        return 1
    else:
        return n+ natural(n-1)
n=int(input("enter a number:"))    
print(natural(n))  
            