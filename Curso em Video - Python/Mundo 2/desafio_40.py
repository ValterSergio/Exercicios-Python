"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
if 7 > media >= 5:
    print(f"O aluno está em recuperação, sua média: {media:.2f}")
elif media < 5:
    print(f"O aluno está Reprovado, sua média: {media:.2f}")
else:
    print(f"O aluno está Aprovado, sua média: {media:.2f}")
