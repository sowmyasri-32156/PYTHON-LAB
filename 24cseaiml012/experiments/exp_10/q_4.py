st=input("enter a string:")
rev=''.join(reversed(st))
print(rev)
vowels=0
consonant=0
for i in st:
    if i in "aeiouAIEOU":
        vowels=vowels+1
    else:
        consonant=consonant+1
print("the vowels are :",vowels)
print("the consonants are :",consonant)