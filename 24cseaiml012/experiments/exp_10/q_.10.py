#wap to swap using bitwise 
a=int(input("enter a value:"))
b=int(input("enter anothe value:"))
a=a^b
b=a^b
a=a^b
print("after conversion the value of a:",a)
print("after coversion the value of b :",b)
