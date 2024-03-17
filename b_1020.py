""" b_1020 - Idade em Dias """
ANO = 0
MES = 0
DIA = 0
idade = int(input())

while idade > 0:
    if idade >= 365:
        ANO += 1
        idade -= 365
    elif idade >= 30:
        MES += 1
        idade -= 30
    else:
        DIA += 1
        idade -= 1
print(f"{ANO} ano(s)")
print(f"{MES} mes(es)")
print(f"{DIA} dia(s)")
