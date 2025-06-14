class ContaCorrente:
    def __init__(self, nome_cliente, num_conta, senha, saldo = 0.0):
        self.nome_cliente = nome_cliente
        self.num_conta = num_conta
        #self.agencia = agencia
        self.saldo = saldo
        self.senha = senha
        #self.cheque_especial = cheque_especial
        #self.cartao_credito = cartao_credito
        #self.financeamento = financeamento

    def mostrar_saldo(self):
        print(f"{self.nome_cliente} Saldo disponível: R${self.saldo:.2f}")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"Saque realizado com sucesso! \nSaldo final: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        if valor > 0:
            print(f"Saldo inicial: {self.saldo}")
            self.saldo = self.saldo + valor
            printprint(f"Depósito realizado com sucesso! \nSaldo final: R${self.saldo:.2f}")

    def transferir(self, valor, destinatario):
        if self.num_conta != destinatario.num_conta:
            ContaCorrente.sacar(self, valor)
            ContaCorrente.deposito(destinatario, valor)