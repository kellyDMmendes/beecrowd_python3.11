""" b_1021 - Notas e Moedas"""
CEM = 0
CINQUENTA = 0
VINTE = 0
DEZ = 0
CINCO = 0
DOIS = 0
UM = 0
CINQUENTACENT = 0
VINTEECINCO = 0
DEZCENT = 0
CINCOCENT = 0
UMCENT = 0
CONT = 0
n = float(input())

while n > 0:
    if n >= 100:
        CEM += 1
        n -= 100
    elif n >= 50:
        CINQUENTA += 1
        n -= 50
    elif n >= 20:
        VINTE += 1
        n -= 20
    elif n >= 10:
        DEZ += 1
        n -= 10
    elif n >= 5:
        CINCO += 1
        n -= 5
    elif n >= 2:
        DOIS += 1
        n -= 2
    elif n >= 1:
        UM += 1
        n -= 1
    elif n >= 0.5:
        CINQUENTACENT += 1
        n -= 0.5
    elif n >= 0.25:
        VINTEECINCO += 1
        n -= 0.25
    elif n >= 0.1:
        DEZCENT += 1
        n -= 0.1
    elif n >= 0.05:
        CINCOCENT += 1
        n -= 0.05
    else:
        UMCENT += 1
        n -= 0.01
    n = round(n, 2)
print("NOTAS:")
print(f"{CEM} nota(s) de R$ 100.00")
print(f"{CINQUENTA} nota(s) de R$ 50.00")
print(f"{VINTE} nota(s) de R$ 20.00")
print(f"{DEZ} nota(s) de R$ 10.00")
print(f"{CINCO} nota(s) de R$ 5.00")
print(f"{DOIS} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{UM} moeda(s) de R$ 1.00")
print(f"{CINQUENTACENT} moeda(s) de R$ 0.50")
print(f"{VINTEECINCO} moeda(s) de R$ 0.25")
print(f"{DEZCENT} moeda(s) de R$ 0.10")
print(f"{CINCOCENT} moeda(s) de R$ 0.05")
print(f"{UMCENT} moeda(s) de R$ 0.01")
