
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

result = []

for index, base in enumerate(numbers):
    result.append(base ** index)

print("original list:", numbers)
print("result list:", result)
