
from abc import ABC, abstractmethod

class Funcionario(ABC):
  

  def __init__(self, nome, cargo, salario):
    self.nome = nome
    self.cargo = cargo
    self.salario = salario

  @abstractmethod
  def calcular_pagamento(self):
    pass

  @abstractmethod
  def tirar_ferias(self):
    pass

class Cargo:
 

  def __init__(self, nome, ferias):
    self.nome = nome
    self.ferias = ferias  # Definindo o atributo 'ferias'

class CLT(Funcionario):
 

  def __init__(self, nome, cargo, salario):
    super().__init__(nome, cargo, salario)
    self.horas_trabalhadas = None

  def set_horas_trabalhadas(self, horas_trabalhadas):
    """Define o valor para horas_trabalhadas."""
    if isinstance(horas_trabalhadas, int) and horas_trabalhadas > 0:
      self.horas_trabalhadas = horas_trabalhadas
    else:
      raise ValueError("Valor de horas_trabalhadas inválido.")

  def calcular_pagamento(self):
    if self.horas_trabalhadas is None:
      print("Erro: horas trabalhadas não informadas para", self.nome)
      return

    valor_hora = self.salario / self.horas_trabalhadas
    pagamento_base = valor_hora * self.horas_trabalhadas
    beneficios = self.salario * 0.3  # Considerando 30% de benefícios
    pagamento_total = pagamento_base + beneficios
    print(f"Pagamento de {self.nome}: R$ {pagamento_total:.2f}")

  def tirar_ferias(self):
    print(f"{self.nome} tirou {self.cargo.ferias} dias de férias.")

class PJ(Funcionario):
  """Subclasse para representar um funcionário PJ."""

  def __init__(self, nome, cargo, salario, valor_projeto):
    super().__init__(nome, cargo, salario)
    self.valor_projeto = valor_projeto

  def calcular_pagamento(self):
    print(f"Pagamento de {self.nome}: R$ {self.valor_projeto:.2f}")

  def tirar_ferias(self):
    print(f"{self.nome} não tem direito a férias, pois é PJ.")

class Freelancer(Funcionario):
  """Subclasse para representar um freelancer."""

  def __init__(self, nome, cargo, salario, valor_hora):
    super().__init__(nome, cargo, salario)
    self.valor_hora = valor_hora
    self.horas_trabalhadas = None

  def set_horas_trabalhadas(self, horas_trabalhadas):
    """Define o valor para horas_trabalhadas."""
    if isinstance(horas_trabalhadas, int) and horas_trabalhadas > 0:
      self.horas_trabalhadas = horas_trabalhadas
    else:
      raise ValueError("Valor de horas_trabalhadas inválido.")

  def calcular_pagamento(self):
    if self.horas_trabalhadas is None:
      print("Erro: horas trabalhadas não informadas para", self.nome)
      return

    valor_recebido = self.valor_hora * self.horas_trabalhadas
    print(f"Pagamento de {self.nome}: R$ {valor_recebido:.2f}")

  def tirar_ferias(self):
    print(f"{self.nome} não tem direito a férias, pois é freelancer.")

# Exemplos de uso
cargo_desenvolvedor = Cargo("Desenvolvedor", 30)
cargo_consultor = Cargo("Consultor", 20)
cargo_designer = Cargo("Designer", 25)

funcionario1 = CLT("João Silva", cargo_desenvolvedor, 2500)
funcionario1.set_horas_trabalhadas(160)

funcionario2 = PJ("Maria Oliveira", cargo_consultor, 5000, 10000)
funcionario3 = Freelancer("Pedro Souza", cargo_designer, 100, 40)

funcionario1.calcular_pagamento()
funcionario2.calcular_pagamento()
funcionario3.calcular_pagamento()

funcionario1.tirar_ferias()
funcionario2.tirar_ferias()
funcionario3.tirar_ferias()