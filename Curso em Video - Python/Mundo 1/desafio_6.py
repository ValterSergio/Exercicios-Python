# Este programa lê um número inteiro digitado pelo usuário
# e exibe o dobro, o triplo e a raiz quadrada desse número.

# Solicita ao usuário que insira um número inteiro
n = int(input("Digite um número: \n"))

# Calcula e exibe o dobro do número
# Multiplicamos o número por 2 para obter o dobro
print(f"O dobro de {n} é: {n * 2}!")

# Calcula e exibe o triplo do número
# Multiplicamos o número por 3 para obter o triplo
print(f"O triplo de {n} é: {n * 3}.")

# Calcula e exibe a raiz quadrada do número
# Utilizamos o operador de exponenciação (**)
# com (1/2), que é o mesmo que calcular a raiz quadrada
print(f"A raiz quadrada de {n} é: {n ** (1 / 2)}.")
