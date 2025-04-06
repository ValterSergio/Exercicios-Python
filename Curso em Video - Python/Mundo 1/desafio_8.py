# Programa que lê um valor em metros e exibe suas conversões para várias unidades de medida.
# Este programa mostra o valor convertido para quilômetros, hectômetros, decâmetros, metros,
# decímetros, centímetros e milímetros.

# Solicita ao usuário que insira um valor em metros
# O valor digitado é convertido para inteiro usando int()
n = int(input("Digite um valor em metros: \n"))

# Converte e exibe o valor em quilômetros
# 1 metro equivale a 0,001 quilômetros, então multiplicamos por 0,001
print(f"{n} metros são {n * 0.001} quilômetros.")

# Converte e exibe o valor em hectômetros
# 1 metro equivale a 0,01 hectômetros, então multiplicamos por 0,01
print(f"{n} metros são {n * 0.01} hectômetros.")

# Converte e exibe o valor em decâmetros
# 1 metro equivale a 0,1 decâmetro, então multiplicamos por 0,1
print(f"{n} metros são {n * 0.1} decâmetros.")

# Exibe o valor em metros (valor original)
# Apenas repetimos o valor, já que ele está na unidade solicitada
print(f"{n} metros são {n} metros.")

# Converte e exibe o valor em decímetros
# 1 metro equivale a 10 decímetros, então dividimos por 0.1 (ou multiplicamos por 10)
print(f"{n} metros são {n / 0.1} decímetros.")

# Converte e exibe o valor em centímetros
# 1 metro equivale a 100 centímetros, então dividimos por 0.01 (ou multiplicamos por 100)
print(f"{n} metros são {n / 0.01} centímetros.")

# Converte e exibe o valor em milímetros
# 1 metro equivale a 1000 milímetros, então dividimos por 0.001 (ou multiplicamos por 1000)
print(f"{n} metros são {n / 0.001} milímetros.")
