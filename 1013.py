""" 1013 - O Maior """
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a < b:
    a = b
if a < c:
    a = c
print(f"{a} eh o maior")
