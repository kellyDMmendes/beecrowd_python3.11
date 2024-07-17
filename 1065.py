""" 1065 - Pares entre Cinco Números """
PAR = 0
CONT = 0

while CONT < 5:
    num = int(input())
    if num % 2 == 0:
        PAR += 1
    CONT += 1

print(f"{PAR} valores pares")
