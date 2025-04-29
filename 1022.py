""" 1022 - TDA Racional """
n_testes = int(input())
for _ in range(n_testes):
    parts = input().split()
    N1, D1 = int(parts[0]), int(parts[2])
    op = parts[3]
    N2, D2 = int(parts[4]), int(parts[6])

    if op == '+':
        numerador = N1 * D2 + N2 * D1
        denominador = D1 * D2
    elif op == '-':
        numerador = N1 * D2 - N2 * D1
        denominador = D1 * D2
    elif op == '*':
        numerador = N1 * N2
        denominador = D1 * D2
    elif op == '/':
        numerador = N1 * D2
        denominador = N2 * D1

    a, b = abs(numerador), abs(denominador)
    while b:
        a, b = b, a % b
    numerador_simpl = numerador // a
    denominador_simpl = denominador // a

    print(f'{numerador}/{denominador} = {numerador_simpl}/{denominador_simpl}')