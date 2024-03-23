""" b_1075 - Resto 2 """
CONT = 1
n = int(input())

while CONT <= 10000:
    if CONT % n == 2:
        print(CONT)
    CONT += 1
