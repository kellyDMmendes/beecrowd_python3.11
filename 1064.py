""" 1064 - Positivos e Médias """
POS = 0
MEDIA = 0
CONT = 0

while CONT < 6:
    num = float(input())
    if num > 0:
        POS += 1
        MEDIA += num
    CONT += 1

MEDIA /= POS

print(f"{POS} valores positivos")
print(f"{MEDIA:.1F}")
