d={}
n=int(input("enter number of key value pairs:"))
for i in range(n):
    k=input("enter key:")
    v=input("enter values:")
    d[k]=v
rev={}
for k,v in d.items():
    rev[v]=k
print("\n original dictionary:" ,d)
print("\n reversed dictionary (values as key):",rev)
  