# Programa que calcula o preço de um produto com 5% de desconto.

# Solicita ao usuário o preço do produto
# O valor é convertido para float para permitir valores decimais
n = float(input("Digite o preço de um produto: \nR$"))

# Calcula o valor do desconto (5% do preço)
desconto = n * 5 / 100

# Exibe o preço original e o preço com desconto
print(f"Na liquidação da loja, esse produto de R${n:.2f} está com desconto de 5%, \nou seja, vai custar só R${n - desconto:.2f}.")
