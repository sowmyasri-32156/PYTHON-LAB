# Function to find factorial of a number
def factorial(num):
    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

# Example usage
number = int(input("Enter a number: "))
print(f"Factorial of {number} is: {factorial(number)}")