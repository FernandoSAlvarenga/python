'''3: Funcionários em uma Empresa 
Crie as classes: 
Funcionario (classe base com atributos nome e salario). 
Gerente (herda de Funcionario, com bônus e método adicionar_funcionario()). 
Vendedor (herda de Funcionario, com comissão e 
método calcular_comissao()). 
Crie uma lista de funcionários: 
Inclua objetos de Gerente e Vendedor. 
Mostre: 
O nome e o salário de cada funcionário. O bônus do gerente (se houver). A comissão do vendedor (se houver). 
Adicione um funcionário: Utilize o método adicionar_funcionario() do gerente para incluir um novo 
funcionário na lista.'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")
        
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
        self.funcionario = []
    
    def add_funcionario(self, funcionario):
        self.funcionario.append(funcionario)
        
    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Bônus: R$ {self.bonus:.2f}")
        
class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao
        vendas = 0
        
    def calculo_comissao(self):
        return self.salario * (self.comissao / 100)
    
    def mostrar_dados(self):
        super().mostrar_dados()
        print(f'{self.calculo_comissao():.2f}')
    
funcionarios = []
    
gerente1 = Gerente('Tay', 10000, 4500 )
vendedor1 = Vendedor('Elo', 9000, 95)
vendedor2 = Vendedor("Helena", 8000, 95)

funcionarios.append(vendedor1)
funcionarios.append(vendedor2)

gerente1.add_funcionario(vendedor1)
gerente1.add_funcionario(vendedor2)

print("\n Funcionários:")
for funcionario in funcionarios:
    funcionario.mostrar_dados()

print("\n Dados do Gerente:")
gerente1.mostrar_dados()