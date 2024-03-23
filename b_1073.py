""" b_1073 - Quadrado de Pares """
CONT = 1
n = int(input())

while CONT <= n:
    if CONT % 2 == 0:
        QUAD = CONT**2
        print(f"{CONT}^2 = {QUAD}")
    CONT += 1
