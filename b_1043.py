""" b_1043 - Triângulo """
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a < b + c and b < a + c and c < a + b:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")
