class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente. Operação de saque não realizada.")

    def consultar_saldo(self):
        return self.saldo

conta1 = ContaBancaria("João", 1000)
conta1.depositar(500)
conta1.sacar(300)

print(f"Saldo de {conta1.titular}: R${conta1.consultar_saldo()}")
