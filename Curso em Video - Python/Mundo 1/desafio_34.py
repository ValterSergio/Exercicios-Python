"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

salario_atual = float(input("Digite seu salário: \n"))
if salario_atual > 1250:
    salario_reajustado = salario_atual + (salario_atual * 10 / 100)
    print(f"Com o aumento de 10%, o seu salário foi de R${salario_atual:.2f} para R${salario_reajustado:.2f}.")
else:
    salario_reajustado = salario_atual  * 1.15
    print(f"Com o aumento de 15%, o seu salário foi de R${salario_atual:.2f} para R${salario_reajustado:.2f}.")
