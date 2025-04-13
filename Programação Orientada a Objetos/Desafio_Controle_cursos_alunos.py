class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir_detalhes(self):
        print(f"Aluno: {self.nome} - Idade: {self.idade}")

class Curso:
    def __init__(self, nome_curso, carga_horaria):
        self.nome_curso = nome_curso
        self.carga_horaria = carga_horaria
        self.turma = []

    def adicionar_aluno(self, nome, idade):
        aluno = Aluno(nome, idade)
        self.turma.append(aluno)
    
    def listar_alunos(self):
        print('-'*79)
        print(f'{"-" * 5} Lista de alunos da turma de {self.nome_curso} {"-" * 5}')
        print('-'*79)
        for aluno in self.turma:
            aluno.exibir_detalhes()
        print('-'*79)
    
    def exibir_resumo(self):
        print('-'*79)
        print(f"Curso: {self.nome_curso} --- Carga Hóraria: {self.carga_horaria} --- Alunos Matriculados: {len(self.turma)}")
        print('-'*79)
    

if __name__ == "__main__":
    curso = Curso("Programação Python", 40)
    curso.adicionar_aluno("Ana", 22)
    curso.adicionar_aluno("Carlos", 30)
    curso.adicionar_aluno("Bruna", 25)

    curso.listar_alunos()
    curso.exibir_resumo()

