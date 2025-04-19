from datetime import datetime


class Livro:
    """Representa um livro com título, autor e ano de publicação."""

    def __init__(self, titulo: str, autor: str, ano_de_publicacao: int):
        """
        Inicializa os atributos de um livro.

        Args:
            titulo (str): Título do livro.
            autor (str): Nome do autor do livro.
            ano_de_publicacao (int): Ano em que o livro foi publicado.
        """
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao


class Usuario:
    """Representa um usuário da biblioteca."""

    def __init__(self, nome: str, cpf: str, email: str):
        """
        Inicializa os atributos de um usuário.

        Args:
            nome (str): Nome completo do usuário.
            cpf (str): CPF do usuário.
            email (str): Endereço de e-mail do usuário.
        """
        self.nome = nome
        self.cpf = cpf
        self.email = email


class RegistroEmprestimo:
    """Representa um empréstimo de um livro feito por um usuário."""

    def __init__(self, usuario: Usuario, livro: Livro, data_emprestimo: datetime, data_devolucao: datetime):
        """
        Inicializa um novo registro de empréstimo.

        Args:
            usuario (Usuario): O usuário que realizou o empréstimo.
            livro (Livro): O livro emprestado.
            data_emprestimo (datetime): Data em que o livro foi emprestado.
            data_devolucao (datetime): Data prevista para devolução.
        """
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao


class SistemaEmprestimos:
    """Gerencia todos os empréstimos de livros da biblioteca."""

    def __init__(self):
        """Inicializa o sistema com uma lista vazia de empréstimos."""
        self.emprestimos = []

    def emprestar_livro(self, usuario: Usuario, livro: Livro, data_emprestimo: datetime, data_devolucao: datetime):
        """
        Registra um novo empréstimo de livro.

        Args:
            usuario (Usuario): Usuário que está pegando o livro emprestado.
            livro (Livro): Livro a ser emprestado.
            data_emprestimo (datetime): Data do empréstimo.
            data_devolucao (datetime): Data prevista de devolução.
        """
        emprestimo = RegistroEmprestimo(usuario, livro, data_emprestimo, data_devolucao)
        self.emprestimos.append(emprestimo)

    def exibir_emprestimos(self):
        """Exibe todos os empréstimos registrados."""
        if not self.emprestimos:
            print("Nenhum empréstimo registrado.")
            return

        print("\n--- Lista de Empréstimos ---\n")
        for emprestimo in self.emprestimos:
            print(f"Usuário: {emprestimo.usuario.nome} (CPF: {emprestimo.usuario.cpf})")
            print(f"Livro: {emprestimo.livro.titulo} | Autor: {emprestimo.livro.autor} | Publicado em: {emprestimo.livro.ano_de_publicacao}")
            print(f"Data do Empréstimo: {emprestimo.data_emprestimo.strftime('%d/%m/%Y')}")
            print(f"Data de Devolução: {emprestimo.data_devolucao.strftime('%d/%m/%Y')}")
            print("-" * 50)


# Execução do sistema
if __name__ == "__main__":
    # Criando usuários
    usuario1 = Usuario("Maria Silva", "12345678900", "maria@email.com")
    usuario2 = Usuario("João Souza", "98765432100", "joao@email.com")

    # Criando livros
    livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    livro2 = Livro("1984", "George Orwell", 1949)

    # Criando sistema de empréstimos
    sistema = SistemaEmprestimos()

    # Registrando empréstimos
    sistema.emprestar_livro(usuario1, livro1, datetime(2025, 4, 18), datetime(2025, 4, 25))
    sistema.emprestar_livro(usuario2, livro2, datetime(2025, 4, 18), datetime(2025, 4, 28))

    # Exibindo empréstimos registrados
    sistema.exibir_emprestimos()
