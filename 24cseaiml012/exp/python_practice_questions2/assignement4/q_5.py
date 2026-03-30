def even(n):
    s=[]
    for i in n:
        if i%2==0:
            s.append(i)
    return s 
x=int(input("enter the list elements:")) 
n=[int(i) for i in x.split(",")]
s=even(n)
print(s)
