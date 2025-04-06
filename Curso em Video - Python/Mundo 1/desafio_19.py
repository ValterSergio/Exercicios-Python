# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.

from random import choice

# a resposta mais rapida que encontrei
alunos = ['paulo', 'fernanda', 'wagner', 'vitor']
print(f"O aluno escolhido de hoje é : {choice(alunos)}")

# minha proposta hoje 
alunos = []
total_alunos = int(input("Quantos alunos vão ser adicionados ao sorteio: "))
for _ in range(total_alunos):
    aluno = input("Informe o nome do aluno: ")
    alunos.append(aluno)

del total_alunos, aluno
print(f"O aluno escolhido de hoje é: {choice(alunos)}")

