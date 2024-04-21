""" b_1134 - Tipo de Combustível """
ALCOOL = 0
GASOLINA = 0
DIESEL = 0
comb = int(input())
while comb != 4:
    if comb == 1:
        ALCOOL += 1
    elif comb == 2:
        GASOLINA += 1
    elif comb == 3:
        DIESEL += 1
    comb = int(input())
print("MUITO OBRIGADO")
print(f"Alcool: {ALCOOL}")
print(f"Gasolina: {GASOLINA}")
print(f"Diesel: {DIESEL}")
