# Programa que lê uma entrada do teclado e exibe informações sobre ela.
# Inclui verificações de tipo e características da string.

# Solicita ao usuário que digite algo
entrada = input('Digite algo: \n')

# Mostra o tipo primitivo do dado inserido (geralmente será 'str')
print(f'Tipo primitivo: {type(entrada)}.')

# Verifica se a entrada é composta apenas por números
# Alternativa sem f-strings (concatenação com str())
print('É numérico? ' + str(entrada.isnumeric()))

# Verifica se a entrada contém apenas letras (alfabética)
print(f'É alfanumérico? {entrada.isalpha()}')

# Verifica se a entrada é composta por caracteres decimais
# Alternativa com concatenação manual
print('É um decimal? ' + str(entrada.isdecimal()))

# Verifica se a entrada está em letras minúsculas
# Alternativa sem f-string
print('Está em caixa baixa? ', entrada.islower())

# Verifica se a entrada contém apenas espaços em branco
print(f'É apenas espaço em branco? {entrada.isspace()}')

# Verifica se a entrada está em letras maiúsculas
# Alternativa usando concatenação manual
print('Está em caixa alta? ' + str(entrada.isupper()))
