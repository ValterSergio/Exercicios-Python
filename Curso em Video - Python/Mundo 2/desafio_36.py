"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

# entrada
valor_casa = float(input("Qual o valor da casa? "))
salario_comprador = float(input("Informe o salário mensal do comprador: "))
anos_pagamento = int(input("Em quantos anos pretende pagar? "))

# processamento
quantidade_prestacoes = anos_pagamento * 12  
valor_prestacao = valor_casa / quantidade_prestacoes
limite_parcela = salario_comprador * 0.3

# saida
if valor_prestacao > limite_parcela:
    print(f"Empréstimo negado! A parcela de R$ {valor_prestacao:.2f} excede 30% do salário.")
else:
    print("Empréstimo aprovado! Pagamento será de R$ {:.2f} mensais.".format(valor_prestacao))
