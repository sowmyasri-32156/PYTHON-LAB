cel = list(map(int, input('Enter temp in C:').split()))
far =[(32 + 9/5 * c) for c in cel]

print('Temp in far is: ', end='')
for i in far:
    print(i, end=' ')                  