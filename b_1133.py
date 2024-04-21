""" b_1133 - Resto da Divisão """
x = int(input())
y = int(input())
for i in range(x, y+1):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
