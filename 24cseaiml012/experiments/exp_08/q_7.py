# Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"   # include both lowercase and uppercase vowels
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage
text = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(text))                            