""" 1097 - Sequencia IJ 3 """

i = 1
j = J = 7

while i <= 9:
    J += 2
    j = J
    while j >= J - 2:
        print(f"I={i} J={j}")
        j -= 1
    i += 2
