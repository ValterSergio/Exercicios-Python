# Programa que lê um número inteiro e exibe sua tabuada (multiplicações de 1 a 10).

# Solicita ao usuário que insira um número inteiro
# O valor digitado é convertido de string para inteiro usando int()
n = int(input('Digite um número: \n'))

# Exibe a mensagem inicial com o número escolhido
# O f-string formata o número dentro da mensagem, indicando qual número está sendo usado na tabuada
print(f'Tabuada do {n}\n:')
print(f'{n} x 1 = {n * 1}')
print(f'{n} x 2 = {n * 2}')
print(f'{n} x 3 = {n * 3}')
print(f'{n} x 4 = {n * 4}')
print(f'{n} x 5 = {n * 5}')
print(f'{n} x 6 = {n * 6}')
print(f'{n} x 7 = {n * 7}')
print(f'{n} x 8 = {n * 8}')
print(f'{n} x 9 = {n * 9}')
print(f'{n} x 10 = {n * 10}')
