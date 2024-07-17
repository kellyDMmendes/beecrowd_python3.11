""" 1010 - Cálculo Simples """
CONT = 0
VALOR = 0

while CONT < 2:
    cod, numPecas, valUnit = input().split()
    cod = int(cod)
    numPecas = int(numPecas)
    valUnit = float(valUnit)

    valor = numPecas * valUnit
    VALOR += valor
    CONT += 1

print(f"VALOR A PAGAR: R$ {VALOR:.2f}")
