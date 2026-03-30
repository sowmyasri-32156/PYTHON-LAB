num1=int(input("enter a number:"))
if num1 <= 1:
    print("is not a prime number" ,num1)
else:
    i = 2
    is_prime = True 
    while i < num1:
        if num1%i == 0:
            is_prime = False 
            break
        i  