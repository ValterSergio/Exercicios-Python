# Programa que converte temperatura de Celsius para Fahrenheit.

# Solicita ao usuário a temperatura em Celsius
# O valor é convertido para float para permitir valores decimais
celsius = float(input("Digite a temperatura em Celsius: \n"))

# Converte Celsius para Fahrenheit utilizando a fórmula: (C * 1.8) + 32
farenheit = (1.8 * celsius) + 32

# Exibe a temperatura em Celsius e o valor correspondente em Fahrenheit
print(f"{celsius}ºC correspondem a {farenheit:.1f}ºF.")
