""" 1046 - Tempo de Jogo """
hi, hf = input().split()
hi = int(hi)
hf = int(hf)

if hi < hf:
    duracao = hf - hi
    print(f"O JOGO DUROU {duracao} HORA(S)")
else:
    duracao = (24 - hi) + hf
    print(f"O JOGO DUROU {duracao} HORA(S)")
