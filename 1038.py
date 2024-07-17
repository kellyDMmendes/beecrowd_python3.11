""" 1038 - Lanche """
cod, quant = input().split()
cod = int(cod)
quant = int(quant)

if cod == 1:
    total = quant * 4
elif cod == 2:
    total = quant * 4.5
elif cod == 3:
    total = quant * 5
elif cod == 4:
    total = quant * 2
else:
    total = quant * 1.5
print(f"Total: R$ {total:.2f}")
