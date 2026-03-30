# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False   # 0 and 1 are not prime
    for i in range(2, int(num**0.5) + 1):  # check divisibility up to sqrt(num)
        if num % i == 0:
            return False
    return True

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a Prime number")
else:
    print(number, "is NOT a Prime number")