""" 1040 - Média 3 """
n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10
print(f"Media: {media:.1f}")

if media < 5:
    print("Aluno reprovado.")
elif media >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno em exame.")
    n = float(input())
    print(f"Nota do exame: {n:.1f}")
    media = (media + n) / 2
    if media < 5:
        print("Aluno reprovado.")
    else:
        print("Aluno aprovado.")
    print(f"Media final: {media:.1f}")
