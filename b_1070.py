""" b_1070 - Seis Números Ímpares """
IMP = 0
x = int(input())

while IMP < 6:
    if x % 2 != 0:
        print(x)
        IMP += 1
    x += 1
