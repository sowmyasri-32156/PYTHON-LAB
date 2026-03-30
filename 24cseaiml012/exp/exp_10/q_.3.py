#wap python program to check whether the number is perfect number or not
# Program to check if a number is a Perfect Number

def is_perfect(num):
    if num < 1:
        return False
    
    sum_of_divisors = 0
    
    # Find divisors and add them
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    
    return sum_of_divisors == num

# Input from user
number = int(input("Enter a number: "))

if is_perfect(number):
    print(f"{number} is a Perfect Number.")
else:
    print(f"{number} is not a Perfect Number.")