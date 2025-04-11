class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def get_nome(self):
        """Obtem o titular da conta"""
        return self._titular
    
    def set_nome(self, novo_titular):
        """Altera o nome do titular"""
        self._titular = novo_titular
    
    def get_saldo(self):
        """Obtem o saldo atual"""
        return self._saldo
    
    def set_saldo(self, novo_saldo):
        """Altera o saldo atual"""
        if novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("Não pode ter saldo negativo")

    def sacar(self, quantia):
        """Realiza o saque se o saldo disponivel for suficiente"""
        if self.get_saldo() >= quantia:
            saldo_atual = self.get_saldo() - quantia
            self.set_saldo(saldo_atual)
        else:
            print("Saldo insuficiente para saque")

    def depositar(self, quantia):
        """Realiza o deposito se o valor para deposito for positivo"""
        if quantia > 0:
            saldo_atual = self.get_saldo() + quantia
            self.set_saldo(saldo_atual)
        else:
            print("Não se pode depositar dividas :) ")

    def exibir_detalhes(self):
        print("-" * 100)
        print(f"Cliente: {self.get_nome()} | Saldo: R$ {self.get_saldo():,.2f} |")
        print("-" * 100)

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)
    
    def cobrar_taxa_mensal(self):
        """Cobra uma taxa mensal de R$ 20,00 ao mês"""
        saldo_atual = self.get_saldo()
        if saldo_atual >= 20:
            self.set_saldo(saldo_atual - 20)
        else:
            print("Saldo Insuficiente, para cobrança da taxa")

    def exibir_detalhes(self):
        print("-" * 100)
        print(f"Tipo: Conta Corrente | Cliente: {self.get_nome()} | Saldo: {self.get_saldo():,.2f} | Taxa de Cartão: R$ 20,00 Mensal")
        print("-" * 100)

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def render_juros(self):
        """Aumenta o saldo em 5%"""
        saldo_atual = self.get_saldo()
        if saldo_atual > 0:
            rendimento = saldo_atual + (saldo_atual * 0.05)
            self.set_saldo(rendimento)
    
    def exibir_detalhes(self):
        print("-" * 100)
        print(f"Tipo: Conta Poupança | Cliente: {self.get_nome()} | Saldo: {self.get_saldo():,.2f} | Taxa de Rendimento: 5% Mensal")
        print("-" * 100)


if __name__ == "__main__":
    
    # TESTES COM CONTA BANCÁRIA
    cliente1 = ContaCorrente("Anderson", 1000)
    cliente5 = ContaCorrente("Silva", 1234.56)
    cliente2 = ContaPoupanca("José", 650)
    cliente3 = ContaPoupanca("Jorge", 350)
    cliente4 = ContaBancaria("Pedro", 986)
    cliente6 = ContaBancaria("Amando", 98765.43)

    clientes = [cliente1, cliente5, cliente2, cliente3, cliente4, cliente6]

    for cliente in clientes:
        cliente.exibir_detalhes()