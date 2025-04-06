from datetime import datetime

dia = int(input("Informe dia de nascimento: "))
mes = int(input("Informe mes de nascimento: "))
ano = int(input("Informe ano de nascimento: "))

data_nascimento = datetime(ano, mes, dia)
data_atual = datetime.now()
idade = (data_atual - data_nascimento).days // 365
print(idade)
if idade == 18:
    print(f"O jovem tem {idade:.0f} anos, e está na hora exata de se alistar !!! ")
elif idade > 18:
    print(f"O jovem tem {idade:.0f} anos, e passou da hora de se alistar !!! ")
else:
    print(f"O jovem tem {idade:.0f} anos, e ainda não está na hora de se alistar !!! ")
