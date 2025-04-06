# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza

nome = input("Digite o nome completo: ").lower()
print(f"Primeiro Nome: {nome.split()[0].capitalize()}")
print(f"Ultimo Nome: {nome.split()[-1].capitalize()}")