"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""

from random import choice

computador = choice(range(5))

print(f"Adivinhe o numero! entre 0 a 5 ")


palpite = int(input("Digite um numero de 0 a 5 para tentar acertar o numero: \n"))

if computador >= palpite:
    print("Palpite muito baixo, você errou !!!")
elif computador <= palpite:
    print("Palpite muito Alto, você errou !!!")
else:
    print("Parabens você acertou o numero é ", computador, '!!!')