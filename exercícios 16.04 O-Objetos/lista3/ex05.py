'''Crie as classes: 
Conta (classe base com atributos titular, saldo e 
métodos depositar(), sacar() e consultar_saldo()). 
ContaPoupanca (herda de Conta, com taxa de juros e método render_juros()). 
ContaCorrente (herda de Conta, com limite de cheque especial). 
Crie contas para diferentes clientes: 
Conta Poupança e Conta Corrente. 
Realize operações: 
Deposite e saque valores em cada conta. Consulte o saldo de cada conta. 
Renda juros na Conta Poupança (se aplicável). 
Utilize o cheque especial da Conta Corrente (se disponível).'''

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso na conta de {self.titular}!")
        else:
            print("Valor inválido para depósito.")
            
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'O valor {valor} foi retirado da sua Conta. Sr(a) {self.titular}, lembrese -se, nunca compartilhe sua senha com estranhos.')
        else:
            print(f'Saldo insuficiente, saldo em conta é: {self.saldo}')
            
    def consulta_saldo(self):
        print(f'Olá {self.titular}, seu saldo é {self.saldo}')
        
class Conta_Poupanca(Conta):
    def __init__(self, titular, saldo, taxa_juros):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros
        
    def calculo_rendimento(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros
        print(f'Olá {self.titular}, voce teve {self.taxa_juros} de rendimento.')
        print(f'Seu saldo atualizado é: {self.saldo}')
        
class Conta_Corrente(Conta):
    def __init__(self, titular, saldo, cheque_especial):
        super().__init__(titular, saldo)
        self.cheque_especial = cheque_especial
    
    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso na conta de {self.titular}!")
            else:
                saldo_cheque_especial = self.cheque_especial - (self.saldo - valor)
        
            if saldo_cheque_especial >= 0:
                self.saldo -= valor
                self.cheque_especial -= self.saldo_cheque_especial
                print(f"Saque de R${valor:.2f} realizado utilizando o cheque especial da conta de {self.titular}!")
            else:
                print("Saldo insuficiente e limite do cheque especial indisponível.")
                
