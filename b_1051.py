""" b_1051 - Imposto de Renda """
IMPOSTO = 0
ISENTO = 0
salario = float(input())

if salario <= 2000:
    print("Isento")
    ISENTO = 1
elif salario > 4500:
    renda = salario - 4500
    salario -= renda
    IMPOSTO += (renda * (28 / 100))
if salario > 3000:
    renda = salario - 3000
    salario -= renda
    IMPOSTO += (renda * (18 / 100))
if salario > 2000:
    renda = salario - 2000
    salario -= renda
    IMPOSTO += (renda * (8 / 100))
if ISENTO == 0:
    print(f"R$ {IMPOSTO:.2f}")
