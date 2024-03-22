class Conta:
    def __init__(self, cliente, agencia, saldo, limite=1000):
        self.cliente = cliente
        self.agencia = agencia
        self. saldo = saldo
        self.limite = limite


    def extrato (self):
        print(f"O saldo de {self.cliente} é R${self.saldo} reais")

    def saque (self, valor):
        self.saldo -= valor


    def deposito (self, valor):
        self.saldo += valor




cliente1 = Conta("Aldair", 5252, 55.50, 1000)
cliente2 = Conta("José", 1717, 100.50, 1000)


cliente1.extrato()
cliente1.deposito(150)
cliente1.extrato()