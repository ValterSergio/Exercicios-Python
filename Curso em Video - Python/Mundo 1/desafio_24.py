# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

# metodo hoje
cidade = input("Digite o nome de uma cidade: ").lower()

print("A cidade tem santo no nome" if 'santo' in cidade else 'A cidade não tem santo no nome.')