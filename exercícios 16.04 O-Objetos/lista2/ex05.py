''' 5. Classe Funcionario e Gerente: 
Crie uma classe Funcionario com os 
atributos nome, cargo, salario e data_admissao. 
Crie uma classe Gerente que herde de Funcionario. 
Adicione à classe Gerente os atributos bonus e area_gerenciada. 
Implemente 
métodos calcular_pagamento(), bonificar(), promover() e apresentar_dad
os() nas classes Funcionario e Gerente. 
Crie objetos funcionario1 e gerente1 e chame os métodos adequados.'''

class Funcionario:
    def __init__(self, nome, cargo, salario, admissao):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.admissao = admissao
    
    def calcular_pgto(self):
        return self.salario
    
    def apresentar_dados(self):
        print(f'O nome do(a) funcionário(a) é: {self.nome}')
        print(f'O cargo do(a) {self.nome} é {self.cargo}')
        print(f'A remuneração atual do(a) {self.nome} é R$: {self.salario}')
        print(f'O(A) {self.nome} esta na empresa desde {self.admissao}')
        
class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, admissao, bonus, setor_de_gestao):
        super().__init__(nome, cargo, salario, admissao)
        self.bonus = bonus
        self.setor_de_gestao = setor_de_gestao
        
    def calcular_pgto(self):
        return self.salario + self.bonus
    
    def apresentar_dados(self):
        super().apresentar_dados()
        print(f'O bonus é R$: {self.bonus}')
        print(f'A área gerenciada é: {self.setor_de_gestao}')

funcionario1 = Funcionario('Tay', "Enfermeira", 6500, 2019 )
gerente1 = Gerente('Eloise', 'Gerente', 10000, 2019, 4000, "T.I." )

print("\n Funcionário:")
funcionario1.apresentar_dados()

print("\n Gerente:")
gerente1.apresentar_dados()
        