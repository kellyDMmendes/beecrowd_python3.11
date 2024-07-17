""" 1142 - PUM """
PUM = 1
n = int(input())
for i in range(n):
    for j in range(3):
        print(PUM, end=" ")
        PUM += 1
    print("PUM")
    PUM += 1
