class ContaBancaria:
    def __init__(self):
        self._saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente")

    def ver_saldo(self):
        return self._saldo


c = ContaBancaria()
c.depositar(100)
c.sacar(30)
print(c.ver_saldo())