

class Pessoa:
    """
    Classe base para representar uma pessoa com nome e CPF.
    """
    def __init__(self, nome: str, cpf: str):
        """
        Inicializa uma nova pessoa.

        :param nome: Nome da pessoa.
        :param cpf: CPF da pessoa.
        """
        self._nome = nome
        self._cpf = cpf

    def get_nome(self) -> str:
        """
        Retorna o nome da pessoa.

        :return: Nome.
        """
        return self._nome

    def get_cpf(self) -> str:
        """
        Retorna o CPF da pessoa.

        :return: CPF.
        """
        return self._cpf


class Professor(Pessoa):
    """
    Representa um professor, herda de Pessoa e armazena disciplinas.
    """
    def __init__(self, nome: str, cpf: str):
        """
        Inicializa um professor com lista de disciplinas vazia.

        :param nome: Nome do professor.
        :param cpf: CPF do professor.
        """
        super().__init__(nome, cpf)
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        """
        Adiciona uma disciplina à lista de disciplinas do professor.

        :param disciplina: Instância da classe Disciplina.
        """
        self.disciplinas.append(disciplina)

    def exibir_dados(self):
        """
        Exibe o nome do professor e suas disciplinas.
        """
        print(f"\nProfessor: {self.get_nome()}")
        print("Disciplinas:")
        for d in self.disciplinas:
            print(f" - {d.get_nome()}")


class Aluno(Pessoa):
    """
    Representa um aluno, herda de Pessoa e possui uma lista de matrículas.
    """
    def __init__(self, nome: str, cpf: str):
        """
        Inicializa um aluno com lista de matrículas vazia.

        :param nome: Nome do aluno.
        :param cpf: CPF do aluno.
        """
        super().__init__(nome, cpf)
        self.matriculas = []

    def matricular(self, turma):
        """
        Matricula o aluno em uma turma.

        :param turma: Instância da classe Turma.
        """
        self.matriculas.append({"turma": turma, "nota": None})
        turma.adicionar_aluno(self)

    def receber_nota(self, turma_nome: str, nota: float):
        """
        Registra a nota do aluno em uma turma específica.

        :param turma_nome: Nome da turma.
        :param nota: Nota a ser atribuída.
        """
        for matricula in self.matriculas:
            if matricula["turma"].nome == turma_nome:
                matricula["nota"] = nota
                break

    def exibir_boletim(self):
        """
        Exibe o boletim do aluno com suas notas por turma.
        """
        print(f"\nBoletim de {self.get_nome()}")
        for matricula in self.matriculas:
            turma = matricula["turma"]
            nota = matricula["nota"]
            print(f"Turma: {turma.nome} | Disciplina: {turma.disciplina.get_nome()} | Nota: {nota}")


class Disciplina:
    """
    Representa uma disciplina com nome e carga horária.
    """
    def __init__(self, nome: str, carga_horaria: int):
        """
        Inicializa uma disciplina.

        :param nome: Nome da disciplina.
        :param carga_horaria: Carga horária total.
        """
        self._nome = nome
        self._carga_horaria = carga_horaria

    def get_nome(self):
        """
        Retorna o nome da disciplina.

        :return: Nome da disciplina.
        """
        return self._nome


class Turma:
    """
    Representa uma turma com nome, turno, disciplina, professor e lista de alunos.
    """
    def __init__(self, nome: str, disciplina: Disciplina, professor: Professor, turno: str = "Manhã"):
        """
        Inicializa uma turma com disciplina, professor e turno.

        :param nome: Nome da turma.
        :param disciplina: Instância da classe Disciplina.
        :param professor: Instância da classe Professor.
        :param turno: Turno da turma (padrão: Manhã).
        """
        self.nome = nome
        self.turno = turno
        self.disciplina = disciplina
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        """
        Adiciona um aluno à turma.

        :param aluno: Instância da classe Aluno.
        """
        self.alunos.append(aluno)

    def exibir_turma(self):
        """
        Exibe os dados da turma, incluindo professor e alunos matriculados.
        """
        print(f"\nTurma: {self.nome} | Turno: {self.turno}")
        print(f"Professor: {self.professor.get_nome()} | Disciplina: {self.disciplina.get_nome()}")
        print("Alunos matriculados:")
        for aluno in self.alunos:
            print(f" - {aluno.get_nome()}")

if __name__ == "__main__":
    # Criando professor e disciplina
    prof = Professor("Gustavo Henrique", "111.111.111-11")
    disc = Disciplina("Matemática", 240)
    prof.adicionar_disciplina(disc)

    # Criando turma e vinculando ao professor e disciplina
    turma1 = Turma("1A", disc, prof)

    # Criando alunos
    aluno1 = Aluno("Wando Souza", "222.222.222-22")
    aluno2 = Aluno("Wictor Silva", "333.333.333-33")

    # Matriculando alunos
    aluno1.matricular(turma1)
    aluno2.matricular(turma1)

    # Atribuindo notas
    aluno1.receber_nota("1A", 8.5)
    aluno2.receber_nota("1A", 7.0)

    # Exibindo informações
    prof.exibir_dados()
    turma1.exibir_turma()
    aluno1.exibir_boletim()
    aluno2.exibir_boletim()
