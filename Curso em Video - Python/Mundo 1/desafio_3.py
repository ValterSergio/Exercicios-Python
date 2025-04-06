# Crie um script Python que leia dois números e tente mostrar a soma entre eles

num1 = int(input('Primeiro número: \n'))
num2 = int(input('Segundo número: \n'))

print('A soma é:', num1 + num2)
print('A soma é: %d!' % (num1 + num2)) # similar ao C

print('A soma é: {}!'.format(num1 + num2))
print(f'A soma é {num1 + num2}') # acho mais bonito desse modo 


""" Aula 6 - Primeiros Passos"""
# Crie um programa que leia dois números e mostre a soma entre eles

n1 = int(input("Digite um número: \n"))
n2 = int(input("Digite outro número: \n"))
s = n1 + n2
print(s)