#1010 - Cálculo Simples
cont = 0
valorT = 0

while cont < 2:
    cod, numPecas, valUnit = input().split()

    valor = int(numPecas) * float(valUnit)
    valorT += valor

    cont += 1

print(f'VALOR A PAGAR: R$ {valorT:.2f}')