# Desafio 16: Programa que lê um número real e mostra sua porção inteira.

from math import trunc  # Importa a função trunc que retorna a parte inteira do número

# Solicita ao usuário que insira um número real
num = float(input("Digite um número real: \n"))

# Exibe o número original e sua porção inteira usando cast para int (truncamento implícito)
print(f"O valor digitado é {num} e a sua porção inteira é {int(num)}.")

# Exibe o número original e sua porção inteira usando a função trunc (truncamento explícito)
print(f"O valor digitado é {num} e a sua porção inteira é {trunc(num)}.")
