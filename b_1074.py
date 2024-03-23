""" b_1074 - Par ou Ímpar """
CONT = 0
n = int(input())

while CONT < n:
    x = int(input())
    if x == 0:
        print("NULL")
    elif x % 2 == 0:
        print("EVEN", end=" ")
    else:
        print("ODD", end=" ")

    if x > 0:
        print("POSITIVE")
    elif x < 0:
        print("NEGATIVE")
    CONT += 1
