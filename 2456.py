''' 2456 - Cartas '''
def crescente(lista):
    for i in range(1, len(lista)):
        if lista[i-1] > lista[i]:
            return False
    return True

def decrescente(lista):
    for i in range(1, len(lista)):
        if lista[i-1] < lista[i]:
            return False
    return True

cartas = [int(x) for x in input().split()]
if crescente(cartas):
    print('C')
elif decrescente(cartas):
    print('D')
else:
    print('N')
