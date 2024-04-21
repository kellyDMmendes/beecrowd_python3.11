""" b_1118 - Várias Notas Com Validação """
CONT = 0
MEDIA = 0
NOVO = 1
while NOVO == 1:
    while CONT < 2:
        nota = float(input())
        while nota < 0 or nota > 10:
            print("nota invalida")
            nota = float(input())
        MEDIA += nota
        CONT += 1
    print(f"media = {(MEDIA / 2):.2f}")
    MEDIA = 0
    CONT = 0
    print("novo calculo (1-sim 2-nao)")
    NOVO = int(input())
    while NOVO != 1 and NOVO != 2:
        print("novo calculo (1-sim 2-nao)")
        NOVO = int(input())
