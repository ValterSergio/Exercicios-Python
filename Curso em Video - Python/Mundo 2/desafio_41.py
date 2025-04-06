"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""

from datetime import datetime

ano = 2015#int(input("Digite o ano de nascimento: "))
ano_atual = datetime.now().year

idade = ano_atual - ano

if idade <= 9:
    print(f"Atleta com {idade} anos: MIRIM")
elif idade > 9 and idade <= 14:
    print(f"Atleta com {idade} anos: INFANTIL")
elif idade > 14 and idade <= 19:
    print(f"Atleta com {idade} anos: JUNIOR")
else:
    print(f"Atleta com {idade} anos: SENIOR")