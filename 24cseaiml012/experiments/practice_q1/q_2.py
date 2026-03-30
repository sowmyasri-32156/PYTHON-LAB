def fibonacci(n):
    a=0
    b=1
    if n == 0 or n == 1:
        return a+b
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter a number :"))    
print(fibonacci(n))
for i in range(2 , n+1):
    print(fibonacci(i), end=" ")
