n=int(input("numbers:"))
temp=nrev=0
while(n>0):
    digit=n%10
    rev=(rev*10)+digit
    n=n//10
    if(temp==rev):
        print("the number is palindrome")
    else:
        print("not palindrome")    