ch = input("enter an alphabet:")
if len(ch) !=1 or not ch.isalpha():
    print("invalid input")
else:
    ch = ch.lower()
    if ch in ['a' , 'e' ,'i' ,'o' ,'u']:
        print("the alphabet is vowel")
    else:
        print("the alphabet is consonent")
                