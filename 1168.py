"""1168 - LED"""
led = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
numero = ''
num_leds = 0

n = int(input());
for _ in range(n):
    numero = input()
    for num in numero:
        num_leds += led[int(num)]
    print(f'{num_leds} leds')
    num_leds = 0