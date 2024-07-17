""" 1067 - Números Ímpares """
CONT = 1
x = int(input())

while CONT <= x:
    if CONT % 2 != 0:
        print(CONT)
    CONT += 1
