# Function to calculate Simple Interest
def simple_interest(principal, rate, time):
    SI = (principal * rate * time) / 100
    return SI

# Example usage
P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest (%): "))
T = float(input("Enter Time (in years): "))

print("Simple Interest is:", simple_interest(P, R, T))