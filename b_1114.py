""" b_1114 - Senha Fixa """
senha_correta = 2002
senha = int(input())
while senha != senha_correta:
    print("Senha Invalida")
    senha = int(input())
print("Acesso Permitido")