""" b_1113 - Crescente e Decrescente """
x, y = input().split()
x = int(x)
y = int(y)
while x != y:
    if x < y:
        print("Crescente")
    else:
        print("Decrescente")
    x, y = input().split()
    x = int(x)
    y = int(y)
