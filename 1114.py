""" 1114 - Senha Fixa """
SENHA = 2002
senha = int(input())
while senha != SENHA:
    print("Senha Invalida")
    senha = int(input())
print("Acesso Permitido")
