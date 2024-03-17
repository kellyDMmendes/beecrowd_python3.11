""" b_1018 - Cédulas """
CEM = 0
CINQUENTA = 0
VINTE = 0
DEZ = 0
CINCO = 0
DOIS = 0
UM = 0
n = int(input())
print(n)

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
    else:
        UM += 1
        n -= 1
print(f"{CEM} nota(s) de R$ 100,00")
print(f"{CINQUENTA} nota(s) de R$ 50,00")
print(f"{VINTE} nota(s) de R$ 20,00")
print(f"{DEZ} nota(s) de R$ 10,00")
print(f"{CINCO} nota(s) de R$ 5,00")
print(f"{DOIS} nota(s) de R$ 2,00")
print(f"{UM} nota(s) de R$ 1,00")
