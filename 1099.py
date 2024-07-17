""" 1099 - Soma de Ímpares Consecutivos II """
IMP = 0
n = int(input())
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > y:
        x, y = y, x
    for j in range(x+1, y):
        if j % 2 != 0:
            IMP += j
    print(IMP)
    IMP = 0
