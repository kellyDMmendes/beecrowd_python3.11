""" 1071 - Soma de Ímpares Consecutivos I"""
IMP = 0
x = int(input())
y = int(input())

if x > y:
    n = x
    x = y
    y = n

if x % 2 != 0:
    x += 1

while x < y:
    if x % 2 != 0:
        IMP += x
    x += 1

print(IMP)
