# Desafio 17: Programa que calcula a hipotenusa de um triângulo retângulo

from math import hypot  # Importa a função hypot para calcular a hipotenusa

# Solicita ao usuário o comprimento do cateto oposto
co = float(input("Cateto oposto: \n"))

# Solicita ao usuário o comprimento do cateto adjacente
ca = float(input("Cateto adjacente: \n"))

# Calcula a hipotenusa usando a fórmula de Pitágoras com a função hypot
hi = hypot(co, ca)

# Exibe os valores dos catetos e a hipotenusa com 2 casas decimais
print(f"A hipotenusa dos números {co} e {ca} é {hi:.2f}.")
