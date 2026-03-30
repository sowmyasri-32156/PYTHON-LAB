list = []
n = int(input("Enter the no of elements:"))
for i in range (n):
    list.append(int(input(i)))
    list= list.append(set(list))
    list.sort()
    print(f"sorted list:{list}")