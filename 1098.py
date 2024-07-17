""" 1098 - Sequencia IJ 4 """
i = 0
j = 1
I = 0
J = 0
while i <= 2:
    while J < 3:
        if i == 0 or I / i == 1:
            print(f"I={i:.0f} J={j:.0f}")
        else:
            print(f"I={i} J={j}")
        j += 1
        J += 1
    i += 0.2
    i = round(i, 1)
    I = int(i)
    j = 1 + i
    J = 0
