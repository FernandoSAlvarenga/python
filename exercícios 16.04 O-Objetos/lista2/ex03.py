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
        
    def get_titular(self):
        return self.titular
    
    def get_saldo(self):
        return self.saldo
    
    def get_taxa_juros(self):
        return self.taxa_juros
    
    def apresentar(self):
        print(f'Olá, meu nome é {self.titular}, meu saldo é {self.saldo}, a taxa de juros da minha conta poupança é {self.taxa_juros}% ao mês.')
        
conta1 = Conta_corrente('Fernando', 2500, 0.80)
conta1.apresentar()

class Conta_poupanca(Conta_corrente):
    def __init__(self, titular, saldo, taxa_juros, rendimento_mensal):
        super().__init__(titular, saldo, taxa_juros)
        self.rendimento_mensal = rendimento_mensal
        
    def get_rendimento_mensal(self):
        return self.rendimento_mensal
    
    