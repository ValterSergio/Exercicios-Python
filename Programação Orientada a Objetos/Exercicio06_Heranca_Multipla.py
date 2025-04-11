class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def get_salario(self):
        return self._salario
    
    def set_salario(self, valor):
        if valor > 0:
            self._salario = valor
        else:
            print("Valor de salário inválido.")
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, novo_nome):
        self._nome = novo_nome


class Vendedor:
    def __init__(self, comissao):
        self._comissao = comissao

    def get_comissao(self):
        return self._comissao
    
    def set_comissao(self, valor):
        if valor > 0:
            self._comissao = valor
        else:
            print("Valor da comissão inválido.")
    
    def calcular_comissao(self, total_vendas):
        """Obtem o total de vendas realizada"""
        return self._comissao * total_vendas


# Herança múltipla
class Gerente(Funcionario, Vendedor):
    def __init__(self, nome, salario, comissao):
        Funcionario.__init__(self, nome, salario)
        Vendedor.__init__(self, comissao)

    def exibir_detalhes(self):
        print(f"Gerente: {self.get_nome()} | Salário: R$ {self.get_salario():,.2f} | Comissão: R$ {self.get_comissao():,.2f}")


# Testando
if __name__ == "__main__":
    gerente = Gerente("Mariana", 5000, 0.10)
    gerente.exibir_detalhes()

    # Simulando vendas
    vendas = 20000
    comissao = gerente.calcular_comissao(vendas)
    print(f"Comissão sobre {vendas:,} itens: R$ {comissao:,.2f}")
