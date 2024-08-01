''' 2850 - Papagaio Poliglota '''
import sys
input = sys.stdin.readline
output = sys.stdout.write

entrada = input().strip()
while entrada:
    if entrada == 'esquerda':
        output(f'ingles\n')
    elif entrada == 'direita':
        output(f'frances\n')
    elif entrada == 'nenhuma':
        output(f'portugues\n')
    elif entrada == 'as duas':
        output(f'caiu\n')
    entrada = input().strip()
