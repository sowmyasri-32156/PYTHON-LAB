def str(s):
    if len(s)==0:
        return s
    else:
        return str(s[1:])+s[0]
s=input("enter a string :") 
print("reverse string is :",str(s))   