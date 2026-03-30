sentence = input("Enter a sentence: ")
LIST1 = sentence.split()
print("\nWords with their indices:")
for index, word in enumerate(LIST1):
    print(f"Index {index}: {word}")
LIST2 = list(range(len(LIST1)))
LIST3 = list(zip(LIST2, LIST1))
print("\nLIST3 (Combined List):")
print(LIST3)