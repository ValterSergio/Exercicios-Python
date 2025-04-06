# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

# metodo hoje
pessoa = input("Digite o nome de uma pessoa: ").lower()

print("A pessoa tem silva no nome" if 'silva' in pessoa else 'A pessoa não tem silva no nome.')