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


if __name__ == "__main__":
    
    # criando conta
    cliente1 = ContaBancaria("Valter", 1000)
    
    # exibir conta
    cliente1.exibir_detalhes()

    # realizar deposito
    cliente1.depositar(100)

    # exibir novo saldo
    cliente1.exibir_detalhes() # saldo deve estar com 1100

    # realizar saque
    cliente1.sacar(200)

    # exibir novo saldo
    cliente1.exibir_detalhes() # saldo deve estar em 900

    # alterar titular
    cliente1.set_nome("Valter Tertuliano")

    cliente1.exibir_detalhes()