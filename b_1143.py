""" b_1143 - Quadrado e ao Cubo """
n = int(input())
for i in range(1, n+1):
    x = i
    print(x, end=" ")
    x *= i
    print(x, end=" ")
    x *= i
    print(x)
