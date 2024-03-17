""" b_1036 - Fórmula de Bhaskara """
from math import sqrt
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a == 0:
    print("Impossivel calcular")
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Impossivel calcular")
    else:
        r1 = (-b + sqrt(delta)) / (2 * a)
        r2 = (-b - sqrt(delta)) / (2 * a)
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")
