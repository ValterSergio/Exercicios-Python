# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome_completo = input("Informe Seu Nome Completo: ")

print(f"Nome em MINUSCULAS: {nome_completo.lower()}")
print(f"Nome em MAIUSCULAS: {nome_completo.upper()}")
print(f"Seu nome tem {len(nome_completo.replace(" ", ''))} letras")

pegar_primeiro_nome = nome_completo.split(' ')
print(f'O primeiro nome tem {len(pegar_primeiro_nome[0])} letras')
