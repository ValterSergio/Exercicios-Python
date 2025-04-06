"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

Um ano é bissexto se:
For divisível por 4 e não divisível por 100, ou
For divisível por 400.

"""

ano = int(input("Digite um ano: \n"))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} NÃO é BISSEXTO.")
