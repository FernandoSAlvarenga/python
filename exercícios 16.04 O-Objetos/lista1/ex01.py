class conta_bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def get_titular(self):
        return self.titular

    def get_saldo(self):
        return self.saldo
    
    def set_titular(self, novo_titular):
        self.titular = novo_titular

    def set_saldo(self, nova_saldo):
        self.saldo = nova_saldo
    
    def depositar(self, valor):
        self.saldo += valor

titular1 = conta_bancaria("Fernando", 2500)

print(f"Nome original: {titular1.get_titular()}")  

print(f'Saldo da conta é: {titular1.get_saldo()}')

titular1.set_titular('Ferdinando')
print(f'Novo Titular é {titular1.get_titular()}')

titular1.depositar(500)

print(f'Novo Saldo da conta é: {titular1.get_saldo()}')

