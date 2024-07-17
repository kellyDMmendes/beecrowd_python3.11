""" 1144 - Sequência Lógica """
n = int(input())
for i in range(1, n+1):
    x = i
    print(x, end=" ")
    y = x * i
    print(y, end=" ")
    z = y * i
    print(z)
    x = i
    print(x, end=" ")
    y += 1
    print(y, end=" ")
    z += 1
    print(z)
