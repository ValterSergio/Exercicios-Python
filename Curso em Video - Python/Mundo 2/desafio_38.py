"""
 Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
"""

n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite + um numero inteiro: "))

if n1 > n2:
    print(f'O número {n1} (primeiro valor) é maior que {n2}')
elif n2 > n1:
    print(f'O numero {n2} (segundo valor) é maior que {n1}')
else:
    print("Os dois numero são iguais")