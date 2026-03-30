
m = int(input("Enter starting number (m): "))
n = int(input("Enter ending number (n): "))
LIST1 = []
for i in range(m, n+1):
    LIST1.append(i)
print("\nLIST1:", LIST1)
total_sum = sum(LIST1)
average = total_sum / len(LIST1)
largest = max(LIST1)
smallest = min(LIST1)
print("\nSum of LIST1:", total_sum)
print("Average of LIST1:", average)
print("Largest number in LIST1:", largest)
print("Smallest number in LIST1:", smallest)
LIST2 = []
for num in LIST1:
    if num % 3 != 0:
        LIST2.append(num)
print("\nLIST2 (excluding numbers divisible by 3):", LIST2)
