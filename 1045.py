""" 1045 - Tipos de Triângulos """
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a < b:
    x = a
    a = b
    b = x
if a < c:
    x = a
    a = c
    c = x
if b < c:
    x = b
    b = c
    c = x

if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")
elif a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")
