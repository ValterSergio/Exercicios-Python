class Medico:
    """Representa um médico com nome e especialidade."""

    def __init__(self, nome, especialidade):
        """
        Inicializa um novo objeto Medico.

        Args:
            nome (str): Nome do médico.
            especialidade (str): Especialidade médica do profissional.
        """
        self.nome = nome
        self.especialidade = especialidade


class Paciente:
    """Representa um paciente com nome e idade."""

    def __init__(self, nome, idade):
        """
        Inicializa um novo objeto Paciente.

        Args:
            nome (str): Nome do paciente.
            idade (int): Idade do paciente.
        """
        self.nome = nome
        self.idade = idade


class Consulta:
    """Representa uma consulta médica entre um paciente e um médico."""

    def __init__(self, paciente: Paciente, medico: Medico, data: str, valor: float):
        """
        Inicializa uma nova consulta.

        Args:
            paciente (Paciente): Objeto representando o paciente.
            medico (Medico): Objeto representando o médico.
            data (str): Data da consulta no formato 'dd/mm/aaaa'.
            valor (float): Valor da consulta em reais.
        """
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.valor = valor if valor > 0 else 0.0

    def exibir_consulta(self):
        """Exibe os detalhes da consulta formatados no terminal."""
        print("-" * 50)
        print(f"Data da Consulta: {self.data}")
        print(f"Médico: {self.medico.nome} ({self.medico.especialidade})")
        print(f"Paciente: {self.paciente.nome} | Idade: {self.paciente.idade}")
        print(f"Valor da Consulta: R$ {self.valor:,.2f}")
        print("-" * 50)


class AgendaConsultas:
    """Gerencia uma lista de consultas médicas."""

    def __init__(self):
        """Inicializa uma agenda de consultas vazia."""
        self.consultas = []

    def marcar_consulta(self, paciente: Paciente, medico: Medico, data: str, valor: float):
        """
        Adiciona uma nova consulta à agenda.

        Args:
            paciente (Paciente): O paciente da consulta.
            medico (Medico): O médico responsável.
            data (str): A data da consulta.
            valor (float): O valor cobrado pela consulta.
        """
        consulta = Consulta(paciente, medico, data, valor)
        self.consultas.append(consulta)

    def listar_consultas(self):
        """Exibe todas as consultas cadastradas na agenda."""
        if not self.consultas:
            print("Nenhuma consulta marcada.")
        for consulta in self.consultas:
            consulta.exibir_consulta()

    def buscar_gastos_por_paciente(self, nome_paciente: str):
        """
        Calcula e exibe o total gasto por um paciente específico.

        Args:
            nome_paciente (str): Nome do paciente para busca.
        """
        total_gasto = 0
        for consulta in self.consultas:
            if consulta.paciente.nome.lower() == nome_paciente.lower():
                total_gasto += consulta.valor

        if total_gasto > 0:
            print(f"\nPaciente: {nome_paciente} | Total gasto: R$ {total_gasto:,.2f}")
        else:
            print(f"\nPaciente '{nome_paciente}' não encontrado em nenhuma consulta.")
