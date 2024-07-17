""" 1066 - Pares, Ímpares, Positivos e Negativos """
PAR = 0
IMP = 0
POS = 0
NEG = 0
CONT = 0

while CONT < 5:
    num = int(input())

    if num % 2 == 0:
        PAR += 1
    else:
        IMP += 1

    if num > 0:
        POS += 1
    elif num < 0:
        NEG += 1

    CONT += 1

print(f"{PAR} valor(es) par(es)")
print(f"{IMP} valor(es) impar(es)")
print(f"{POS} valor(es) positivo(s)")
print(f"{NEG} valor(es) negativo(s)")
