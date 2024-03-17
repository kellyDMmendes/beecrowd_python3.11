""" b_1049 - Animal """
palavra = input()

if palavra == "vertebrado":
    palavra = input()

    if palavra == "ave":
        palavra = input()

        if palavra == "carnivoro":
            PALAVRA = "aguia"

        if palavra == "onivoro":
            PALAVRA = "pomba"

    if palavra == "mamifero":
        palavra = input()

        if palavra == "onivoro":
            PALAVRA = "homem"

        if palavra == "herbivoro":
            PALAVRA = "vaca"

if palavra == "invertebrado":
    palavra = input()

    if palavra == "inseto":
        palavra = input()

        if palavra == "hematofago":
            PALAVRA = "pulga"

        if palavra == "herbivoro":
            PALAVRA = "lagarta"

    if palavra == "anelideo":
        palavra = input()

        if palavra == "hematofago":
            PALAVRA = "sanguessuga"

        if palavra == "onivoro":
            PALAVRA = "minhoca"

print(PALAVRA)
