""" b_1131 - Grenais """
CONT = 0
EMPATE = 0
INTER = 0
GREMIO = 0
NOVO = 1
while NOVO == 1:
    inter, gremio = input().split()
    inter = int(inter)
    gremio = int(gremio)
    CONT += 1
    if inter > gremio:
        INTER += 1
    elif gremio > inter:
        GREMIO += 1
    else:
        EMPATE += 1
    print("Novo grenal (1-sim 2-nao)")
    NOVO = int(input())
print(f"{CONT} grenais")
print(f"Inter:{INTER}")
print(f"Gremio:{GREMIO}")
print(f"Empates:{EMPATE}")
if INTER > GREMIO:
    print("Inter venceu mais")
elif GREMIO > INTER:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
