# Programa que lê as duas notas de um aluno, calcula a média entre elas e exibe o resultado.

# Solicita ao usuário que insira a primeira nota
# A função input captura o valor como texto, e usamos float() para convertê-lo para um número decimal
nota1 = float(input('Nota 1: \n'))

# Solicita ao usuário que insira a segunda nota
# Também converte o valor de texto para número decimal (float)
nota2 = float(input('Nota 2: \n'))

# Calcula a média das duas notas e exibe o resultado com uma mensagem formatada
# Utilizamos a média aritmética: soma das notas dividida por 2
# {:.1f} formata os números para mostrar apenas uma casa decimal
print(f'A média das notas {nota1:.1f} e {nota2:.1f} é {((nota1 + nota2) / 2):.1f}!')
