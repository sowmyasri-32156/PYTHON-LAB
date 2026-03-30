#wap to string and print in a reverse order and also print vowels and consonents in it
me = input("Enter a string: ")
print("Reversed string is:", me[::-1])
vowels = "aeiouAEIOU"
for ch in me:
    if ch in vowels:
        print("The vowel is:", ch)
    elif ch.isalpha():  
        print("The consonant is:", ch)        