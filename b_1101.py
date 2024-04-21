""" b_1101 - Sequência de Números e Soma """
SOMA = 0
m, n = input().split()
m = int(m)
n = int(n)
while m > 0 and n > 0:
    if m > n:
        m, n = n, m
    for i in range(m, n+1):
        print(i, end=" ")
        SOMA += i
    print(f"Sum={SOMA}")
    SOMA = 0
    m, n = input().split()
    m = int(m)
    n = int(n)
