# Programa que calcula a área de uma parede e a quantidade de tinta necessária para pintá-la.

# Solicita ao usuário a largura e altura da parede
# A entrada é convertida para float para permitir valores decimais
largura = float(input('Digite a largura: \n'))
altura = float(input('Digite a altura: \n'))

# Calcula a área da parede (largura * altura)
area = largura * altura

# Exibe as dimensões da parede e sua área
print(f'Sua parede tem a dimensão {largura} x {altura} e sua área é de {area}m².')

# Calcula a quantidade de tinta necessária (1 litro cobre 2m²)
tinta_necessaria = area / 2

# Exibe a quantidade de tinta necessária para pintar a parede
print(f"Para pintar essa parede, você precisará de {tinta_necessaria}L de tinta.")
