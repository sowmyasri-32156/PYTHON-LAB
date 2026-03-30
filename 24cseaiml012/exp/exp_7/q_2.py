m = int(input("Enter starting number (m): "))
n = int(input("Enter ending number (n): "))
prime_list = []
for num in range(m, n+1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
print(f"\nPrime numbers between {m} and {n}:")
print(prime_list)