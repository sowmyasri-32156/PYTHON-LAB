def palindrome(s):
    if len(s)==0:
        return s
    else:
        return palindrome(s[1:])+s[0]
s=input("enter a string :")
if s==palindrome(s):
    print("palindrome")
else:
    print("not palindrome")    