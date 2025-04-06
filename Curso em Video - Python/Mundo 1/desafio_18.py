# Desafio 18: Programa que calcula seno, cosseno e tangente de um ângulo fornecido pelo usuário.

from math import sin, cos, tan, radians  # Importa funções trigonométricas e conversão para radianos

# Solicita ao usuário um ângulo (em graus)
ang = float(input("Digite um ângulo de uma circunferência (entre 0º e 360º): \n"))

# Converte o ângulo para radianos e calcula as funções trigonométricas
seno = sin(radians(ang))   # Calcula o seno
coss = cos(radians(ang))   # Calcula o cosseno
tang = tan(radians(ang))   # Calcula a tangente

# Exibe os valores calculados com 2 casas decimais
print(f"O ângulo de {ang} tem o seno de {seno:.2f}.")
print(f"O ângulo de {ang} tem o cosseno de {coss:.2f}.")
print(f"O ângulo de {ang} tem a tangente de {tang:.2f}.")
