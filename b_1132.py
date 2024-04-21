""" b_1132 - Múltiplos de 13 """
SOMA = 0
x = int(input())
y = int(input())
if x > y:
    x, y = y, x
for i in range(x, y+1):
    if i % 13 != 0:
        SOMA += i
print(SOMA)
