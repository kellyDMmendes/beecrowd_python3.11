""" 1048 - Aumento de Salário """
salario = float(input())

if salario <= 400:
    PERCENTUAL = 15
elif salario > 400 and salario <= 800:
    PERCENTUAL = 12
elif salario > 800 and salario <= 1200:
    PERCENTUAL = 10
elif salario > 1200 and salario <= 2000:
    PERCENTUAL = 7
else:
    PERCENTUAL = 4

reajuste = (salario * PERCENTUAL) / 100
salario += reajuste

print(f"Novo salario: {salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {PERCENTUAL} %")
