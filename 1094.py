""" 1094 - Experiências """
TOTAL = 0
C = 0
R = 0
S = 0
CONT = 0
n = int(input())

while CONT < n:
    quantia, tipo = input().split()
    quantia = int(quantia)

    TOTAL += quantia
    if tipo == "C":
        C += quantia
    elif tipo == "R":
        R += quantia
    else:
        S += quantia
    CONT += 1

C_cento = (C * 100) / TOTAL
R_cento = (R * 100) / TOTAL
S_cento = (S * 100) / TOTAL

print(f"Total: {TOTAL} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")
print(f"Percentual de coelhos: {C_cento:.2f} %")
print(f"Percentual de ratos: {R_cento:.2f} %")
print(f"Percentual de sapos: {S_cento:.2f} %")
