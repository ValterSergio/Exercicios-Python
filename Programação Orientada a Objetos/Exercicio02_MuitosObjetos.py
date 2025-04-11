class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_produto(self):
        print(f"| Produto: {self.nome} | Preço: R$ {self.preco:,.2f} |")
    

if __name__ == "__main__":
    p1 = Produto("Lápis", 1.5)
    p2 = Produto("Caneta", 2.55)
    p3 = Produto("Estojo", 4.89)

    lista = [p1, p2, p3]

    for objeto in lista:
        objeto.exibir_produto()
    