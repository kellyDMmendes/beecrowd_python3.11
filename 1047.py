""" 1047 - Tempo de Jogo com Minutos """
hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

if mi <= mf:
    minutos = mf - mi
else:
    minutos = (60 - mi) + mf
    hf -= 1

if hi <= hf and mi != mf:
    horas = hf - hi
else:
    horas = (24 - hi) + hf

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
