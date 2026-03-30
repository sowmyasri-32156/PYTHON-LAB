#wap to enter 5 digit number and print the digit present at odd location
num = input("Enter a 5 digit number: ")
if len(num) != 5:
    print("The number is not a 5 digit number.")
else:
    print("Digits at odd positions are:")
    for i in range(len(num)):
        if (i + 1) % 2 == 1:  
            print("the odd index of the given number is:",num[i])        