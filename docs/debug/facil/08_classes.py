# ────────────────────────────────────────────────────────────
# Nível: Fácil  │  Tema: Classes
# ────────────────────────────────────────────────────────────
#
# O programa define uma classe ContaBancaria com saldo inicial,
# métodos depositar() e sacar(), e __str__ formatado.
#
# Saída esperada (dados fixos no código):
#
#   Depósito de R$ 200.00 realizado.
#   Saque de R$ 100.00 realizado.
#   Conta de Ana, saldo: R$ 600.00
#
# Encontre e corrija o erro antes de rodar.
# ────────────────────────────────────────────────────────────

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo   = saldo_inicial

    def depositar(valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")

    def __str__(self):
        return f"Conta de {self.titular}, saldo: R$ {self.saldo:.2f}"


conta = ContaBancaria("Ana", 500)
conta.depositar(200)
conta.sacar(100)
print(conta)
