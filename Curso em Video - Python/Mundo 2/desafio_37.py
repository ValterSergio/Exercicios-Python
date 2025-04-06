"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

# entrada
n = int(input("Digite um numero inteiro: "))
print('''
      Escolha uma base para conversão: 

[ 1 ] Binario
[ 2 ] Octal
[ 3 ] Hexadecimal
      ''')

escolha = int(input("Escolha entre 1/2/3 para conversão: "))

if escolha == 1:
    print(f'O {n} convertido para binario é {bin(n)}')
elif escolha == 2:
    print(f'O {n} convertido para Octal é {oct(n)}')
elif escolha == 3: 
    print(f'O {n} convertido para Hexadecimal é {hex(n)}')
else:
    print("Informe uma opção valida para conversão.")