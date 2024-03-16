""" b_1012 - Área """
PI = 3.14159
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

triangulo = (a * c) / 2
print(F"TRIANGULO: {triangulo:.3f}")

circulo = PI * c**2
print(f"CIRCULO: {circulo:.3f}")

trapezio = ((a + b) * c) / 2
print(f"TRAPEZIO: {trapezio:.3f}")

quadrado = b * b
print(f"QUADRADO: {quadrado:.3f}")

retangulo = a * b
print(f"RETANGULO: {retangulo:.3f}")
