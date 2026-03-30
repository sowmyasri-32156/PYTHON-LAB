a=0
b=1
sum=0
print("fibonacci series between 0 to 100 is :")
for i in range(100):
    if(a>100):
       break
    print(a,end=",")
    if(a%2==0):
        sum+=a
    temp=a
    a=b
    b=temp+b
print("sum of even terms:",sum)
        