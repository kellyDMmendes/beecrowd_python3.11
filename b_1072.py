""" b_1072 - Intervalo 2 """
IN = 0
OUT = 0
CONT = 0
n = int(input())

while CONT < n:
    x = int(input())
    if x >= 10 and x <= 20:
        IN += 1
    else:
        OUT += 1
    CONT += 1

print(f"{IN} in")
print(f"{OUT} out")
