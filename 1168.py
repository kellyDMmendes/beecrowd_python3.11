""" 1168 - LED """
leds_por_digito = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)

n = int(input())
for _ in range(n):
    numero = input().strip()
    total_leds = sum(leds_por_digito[int(digito)] for digito in numero)
    print(f"{total_leds} leds")