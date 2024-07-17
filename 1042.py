""" 1042 - Sort Simples """
n1, n2, n3 = input().split()
n1 = no1 = int(n1)
n2 = no2 = int(n2)
n3 = no3 = int(n3)

if no1 > no2:
    x = no1
    no1 = no2
    no2 = x
if no1 > no3:
    x = no1
    no1 = no3
    no3 = x
if no2 > no3:
    x = no2
    no2 = no3
    no3 = x
print(f"{no1}\n{no2}\n{no3}\n")
print(f"{n1}\n{n2}\n{n3}")
