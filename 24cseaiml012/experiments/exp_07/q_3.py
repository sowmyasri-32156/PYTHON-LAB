# paragraph = """Madam Arora teaches malayalam. 
# Level civic radar refer wow noon stats are examples of palindromes."""
paragraph=input("enter a paragraph:")
#count how many words it contains. 
words = paragraph.split()
word_count = len(words)
print("Total number of words:", word_count)
# Count how many palindromes exist.
palindrome_count = 0
palindromes = []
for word in words:
    cleaned = word.lower().strip(".,!?")   # remove punctuation
    if cleaned == cleaned[::-1] and len(cleaned) > 1:
        palindrome_count += 1
        palindromes.append(cleaned)
print("Number of palindromes:", palindrome_count)
print("Palindromes found:", palindromes)
#  Print each word in reverse order.
print("\nWords in reverse order:")
for word in words:
    print(word[::-1])
