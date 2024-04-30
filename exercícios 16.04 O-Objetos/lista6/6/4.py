class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial deve ser positivo")
        self.titular = titular
        self.saldo = saldo_inicial

    def __str__(self):
        return f"Conta de: {self.titular}, Saldo: {self.saldo:.2f}"

    def __eq__(self, outra_conta):
        return self.titular == outra_conta.titular and self.saldo == outra_conta.saldo

    def __add__(self, outra_conta):
        nova_conta = ContaBancaria(self.titular, self.saldo + outra_conta.saldo)
        return nova_conta

    def __sub__(self, outra_conta):
        if self.saldo < outra_conta.saldo:
            return None
        nova_conta = ContaBancaria(self.titular, self.saldo - outra_conta.saldo)
        return nova_conta

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("Valor a depositar deve ser positivo")
        self.saldo += valor

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("Valor a sacar deve ser positivo")
        if self.saldo < valor:
            return None
        self.saldo -= valor

# Exemplo de uso
conta1 = ContaBancaria("João", 100)
conta2 = ContaBancaria("Maria", 200)
conta3 = ContaBancaria("Pedro", -50)  # Erro: Saldo inicial deve ser positivo

print(conta1)  # Saída: Conta de: João, Saldo: 100.00
print(conta2)  # Saída: Conta de: Maria, Saldo: 200.00

conta_soma = conta1 + conta2
print(f"Soma das contas 1 e 2: {conta_soma}")  # Saída: Conta de: João, Saldo: 300.00

conta_diferenca = conta1 - conta2
print(f"Diferença entre contas 1 e 2: {conta_diferenca}")  # Saída: Conta de: João, Saldo: -100.00

conta_sacado = conta1.sacar(50)
print(f"Conta 1 após saque de 50: {conta_sacado}")  # Saída: Conta de: João, Saldo: 50.00

conta_deposito = conta2.depositar(100)
print(f"Conta 2 após depósito de 100: {conta_deposito}")  # Saída: Conta de: Maria, Saldo: 300.00

conta_insuficiente = conta1 - conta3
print(f"Subtração das contas 1 e 3: {conta_insuficiente}")  # Saída: None (saldo insuficiente)