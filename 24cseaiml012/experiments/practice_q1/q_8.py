def sum(n):
    if n==0:
        return n
    return (n%10)+sum(n//10)
n=int(input("enter a number:"))
print(sum(n))