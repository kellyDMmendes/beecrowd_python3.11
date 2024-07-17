""" 1117 - Validação de Nota """
MEDIA = 0
CONT = 0
while CONT < 2:
    nota = float(input())
    while nota < 0 or nota > 10:
        print("nota invalida")
        nota = float(input())
    MEDIA += nota
    CONT += 1
print(f"media = {(MEDIA / 2):.2F}")
