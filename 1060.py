""" 1060 - Números Positivos """
POS = 0
CONT = 0

while CONT < 6:
    num = float(input())
    if num > 0:
        POS += 1
    CONT += 1

print(f"{POS} valores positivos")
