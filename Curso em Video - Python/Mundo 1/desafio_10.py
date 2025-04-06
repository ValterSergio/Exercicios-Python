# Programa que lê o valor em reais e converte para dólares com base na cotação

# Solicita ao usuário o valor em reais
n = float(input("Quanto dinheiro você tem? \nR$"))

# Define a cotação do dólar
dolar = 3.27

# Realiza a conversão de reais para dólares
conversao = n / dolar

# Exibe o valor em dólares com duas casas decimais
print(f"Com R${n} você pode comprar US$ {conversao:.2f}.")
