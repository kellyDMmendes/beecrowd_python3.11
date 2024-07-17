""" 1019 - Conversão de Tempo """
HORA = 0
MINUTO = 0
SEGUNDO = 0
n = int(input())

while n > 0:
    if n >= 3600:
        HORA += 1
        n -= 3600
    elif n >= 60:
        MINUTO += 1
        n -= 60
    else:
        SEGUNDO += 1
        n -= 1
print(f"{HORA}:{MINUTO}:{SEGUNDO}")
