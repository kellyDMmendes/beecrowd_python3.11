""" b_1061 - Tempo de um Evento """
x1, diai = input(). split()
horai, x1, mini, x2, segi = input().split()

diai = int(diai)
horai = int(horai)
mini = int(mini)
segi = int(segi)

x1, diaf = input().split()
horaf, x1, minf, x2, segf = input().split()

diaf = int(diaf)
horaf = int(horaf)
minf = int(minf)
segf = int(segf)

if segi <= segf:
    seg = segf - segi
else:
    seg = (60 + segf) - segi
    minf -= 1

if mini <= minf:
    minu = minf - mini
else:
    minu = (60 + minf) - mini
    horaf -= 1

if horai <= horaf:
    hora = horaf - horai
else:
    hora = (24 + horaf) - horai
    diaf -= 1

dia = diaf - diai

print(f"{dia} dia(s)")
print(f"{hora} hora(s)")
print(f"{minu} minuto(s)")
print(f"{seg} segundo(s)")
