def minimum(list):
    if len(list)==1:
        return list[0]
    return min(list[0],minimum(list[1:]))
list=[1,2,3,4,5]
print(minimum(list))    