# Programa que calcula o novo salário de um funcionário com 15% de aumento.

# Solicita ao usuário o salário atual
# O valor é convertido para float para permitir valores decimais
salario = float(input("Digite seu salário: \nR$"))

# Calcula o valor do aumento (15% do salário)
aumento = salario * 15 / 100

# Exibe o salário atual e o novo salário com aumento
print(f"O salário do funcionário, que é de R${salario:.2f}, vai subir para R${salario + aumento:.2f} com o aumento de 15%.")
