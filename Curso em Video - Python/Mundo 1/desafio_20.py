# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunos = []
total_alunos = int(input("Quantos alunos vão ser adicionados ao sorteio: "))
for _ in range(total_alunos):
    aluno = input("Informe o nome do aluno: ")
    alunos.append(aluno)

shuffle(alunos) # embaralha a lista
for aluno in alunos:
    print(aluno)