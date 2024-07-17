""" 1080 - Maior e Posição """
MAIOR = 0
CONT = 1

while CONT <= 100:
    num = int(input())
    if num > MAIOR:
        MAIOR = num
        POS = CONT
    CONT += 1

print(MAIOR)
print(POS)
