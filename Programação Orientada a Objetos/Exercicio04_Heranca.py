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
        print(f"Cliente: {self.get_nome()} | Saldo: R$ {self.get_saldo():,.2f} |")

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

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def render_juros(self):
        """Aumenta o saldo em 5%"""
        saldo_atual = self.get_saldo()
        if saldo_atual > 0:
            rendimento = saldo_atual + (saldo_atual * 0.05)
            self.set_saldo(rendimento)
    


if __name__ == "__main__":
    
    # TESTES COM CONTA BANCÁRIA
    cliente1 = ContaBancaria("Valter", 1000)
    cliente1.exibir_detalhes()
    cliente1.depositar(100)
    cliente1.exibir_detalhes()  # 1100
    cliente1.sacar(200)
    cliente1.exibir_detalhes()  # 900
    cliente1.set_nome("Valter Tertuliano")
    cliente1.exibir_detalhes()

    print("\n--- Testando Conta Corrente ---")
    cliente_conta_corrente = ContaCorrente("Ana", 100)
    cliente_conta_corrente.exibir_detalhes()  # 100
    cliente_conta_corrente.cobrar_taxa_mensal()
    cliente_conta_corrente.exibir_detalhes()  # 80
    cliente_conta_corrente.cobrar_taxa_mensal()
    cliente_conta_corrente.cobrar_taxa_mensal()
    cliente_conta_corrente.exibir_detalhes()  # 40
    cliente_conta_corrente.cobrar_taxa_mensal()  # deve sobrar 20
    cliente_conta_corrente.exibir_detalhes()
    cliente_conta_corrente.cobrar_taxa_mensal()  # deve ir a 0
    cliente_conta_corrente.exibir_detalhes()
    cliente_conta_corrente.cobrar_taxa_mensal()  # saldo insuficiente

    print("\n--- Testando Conta Poupança ---")
    cliente_conta_poupanca = ContaPoupanca("Carlos", 200)
    cliente_conta_poupanca.exibir_detalhes()
    cliente_conta_poupanca.render_juros()
    cliente_conta_poupanca.exibir_detalhes()  # saldo deve estar em 210
    cliente_conta_poupanca.render_juros()
    cliente_conta_poupanca.exibir_detalhes()  # saldo deve estar em 220.5