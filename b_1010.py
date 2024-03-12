""" b_1010 - Cálculo Simples """
CONT = 0
VALOR = 0

while CONT < 2:
    cod, numPecas, valUnit = input().split()

    valor = int(numPecas) * float(valUnit)
    VALOR += valor

    CONT += 1

print(f"VALOR A PAGAR: R$ {VALOR:.2f}")
