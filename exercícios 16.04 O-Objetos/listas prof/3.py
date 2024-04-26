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
    self.funcionarios = []

  def adicionar_funcionario(self, funcionario):
    self.funcionarios.append(funcionario)

  def mostrar_dados(self):
    super().mostrar_dados()
    print(f"Bônus: R$ {self.bonus:.2f}")

class Vendedor(Funcionario):
  

  def __init__(self, nome, salario, comissao):
    super().__init__(nome, salario)
    self.comissao = comissao
    self.vendas = 0

  def calcular_comissao(self):
    return self.vendas * (self.comissao / 100)

  def mostrar_dados(self):
    super().mostrar_dados()
    print(f"Comissão: R$ {self.calcular_comissao():.2f}")

# Criação da lista de funcionários
funcionarios = []

# Criação de objetos de Gerente e Vendedor
gerente1 = Gerente("Maria da Silva", 3500.0, 500.0)
vendedor1 = Vendedor("João Oliveira", 2000.0, 5.0)
vendedor2 = Vendedor("Ana Souza", 1800.0, 7.0)

# Adição de vendedores à lista de funcionários
funcionarios.append(vendedor1)
funcionarios.append(vendedor2)

# Adição de vendedores à lista de funcionários gerenciados pelo gerente
gerente1.adicionar_funcionario(vendedor1)
gerente1.adicionar_funcionario(vendedor2)

# Apresentação dos dados dos funcionários
print("\nFuncionários:")
for funcionario in funcionarios:
  funcionario.mostrar_dados()

print("\nDados do Gerente:")
gerente1.mostrar_dados()