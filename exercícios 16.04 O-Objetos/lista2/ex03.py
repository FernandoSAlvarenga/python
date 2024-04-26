''' . Classe Conta Bancária e Conta Poupança: 
Crie uma classe ContaBancaria com os 
atributos titular, saldo e taxa_juros. 
Crie uma classe ContaPoupanca que herde de ContaBancaria. 
Adicione à classe ContaPoupanca o atributo rendimento_mensal. 
Implemente 
métodos depositar(), sacar(), calcular_rendimento() e apresentar_saldo()
 nas classes ContaBancaria e ContaPoupanca. 
Crie objetos conta1 e conta_poupanca1 e chame os métodos 
adequados.'''

class Conta_corrente:
    def __init__(self, titular, saldo, taxa_juros):
        self.titular = titular
        self.saldo = saldo
        self.taxa_juros = taxa_juros
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def calcular_rendimento(self):
        return self.saldo * self.taxa_juros / 100

    def apresentar_saldo(self):
        print(f"Saldo: {self.saldo:.2f}")
    
class Conta_poupanca(Conta_corrente):
    def __init__(self, titular, saldo, taxa_juros, rendimento_mensal=0):
        super().__init__(titular, saldo, taxa_juros)
        self.rendimento_mensal = rendimento_mensal
        
    def calcular_rendimento(self):
        self.rendimento_mensal += super().calcular_rendimento()
        return self.rendimento_mensal
    
    def apresentar_saldo(self):
        super().apresentar_saldo()
        print(f"Rendimento mensal: {self.rendimento_mensal:.2f}")
    
    
conta1 = Conta_corrente('Fernando', 2500, 0.80)
conta_poupanca1 = Conta_poupanca("Fernando", 2500, 0.92)

print("\n Conta Corrente:")
conta1.depositar(800)
conta1.sacar(500)
conta1.apresentar_saldo()

print("\n Conta Poupança:")
conta_poupanca1.depositar(300)
conta_poupanca1.calcular_rendimento()
conta_poupanca1.sacar(200)
conta_poupanca1.apresentar_saldo()