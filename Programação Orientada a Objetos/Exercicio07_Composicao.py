class ItemPedido:
    """
    Representa um item de um pedido no restaurante.

    Atributos:
        nome (str): Nome do item.
        quantidade (int): Quantidade do item pedido.
        valor_unitario (float): Preço unitário do item.
    """

    def __init__(self, nome, quantidade, valor_unitario):
        """
        Inicializa o item do pedido com nome, quantidade e valor unitário.
        """
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def calcular_total(self):
        """
        Calcula o valor total do item (quantidade × valor unitário).

        Retorna:
            float: Total do item.
        """
        return self.quantidade * self.valor_unitario


class Pedido:
    """
    Representa um pedido feito no restaurante, composto por vários itens.
    """

    def __init__(self):
        """
        Inicializa um pedido com uma lista vazia de itens.
        """
        self.lista_pedido = []

    def adicionar_pedido(self, nome, quantidade, valor_unitario):
        """
        Adiciona um novo item ao pedido.

        Parâmetros:
            nome (str): Nome do item.
            quantidade (int): Quantidade desejada.
            valor_unitario (float): Preço unitário do item.
        """
        pedido = ItemPedido(nome, quantidade, valor_unitario)
        self.lista_pedido.append(pedido)

    def calcular_pedido(self):
        """
        Calcula o valor total do pedido somando todos os itens.

        Retorna:
            float: Total do pedido.
        """
        return sum(pedido.calcular_total() for pedido in self.lista_pedido)

    def exibir_fatura(self):
        """
        Exibe a fatura detalhada com todos os itens do pedido,
        incluindo quantidade, preço unitário e total de cada item.
        """
        print("-" * 50)
        print("\t Restaurante do Tio ")
        print("-" * 50)
        print(f"{'-|-' * 3} Comprovante de compra {'-|-' * 3}")
        print("-" * 50)
        for pedido in self.lista_pedido:
            print(
                f'{pedido.nome} - Quantidade: {pedido.quantidade} - '
                f'Preço: R$ {pedido.valor_unitario:,.2f} - '
                f'Total: R$ {pedido.calcular_total():,.2f}'
            )
        print("-" * 50)
        print(f"Total Geral: R$ {self.calcular_pedido():,.2f}")
        print("-" * 50)

if __name__ == "__main__":
    # Criação do pedido
    pedido = Pedido()

    # Adiciona um item ao pedido
    pedido.adicionar_pedido("Pastel de carne", 3, 5)

    # Exibe a fatura com os detalhes do pedido
    pedido.exibir_fatura()
