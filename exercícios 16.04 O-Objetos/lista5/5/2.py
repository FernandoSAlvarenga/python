from abc import ABC, abstractmethod

class ContaBancaria(ABC):
  """
  Classe abstrata para representar contas bancárias.

  Atributos:
    _titular: Nome do titular da conta (str).
    _saldo: Saldo da conta (float).
    _taxa_juros: Taxa de juros da conta (float, porcentagem anual).

  Métodos abstratos:
    depositar(self, valor): Deposita um valor na conta.
    sacar(self, valor): Realiza um saque na conta.
    calcular_juros(self): Calcula os juros rendidos pela conta (a ser implementado em classes derivadas).
  """

  def __init__(self, titular, saldo, taxa_juros):
    self._titular = titular
    self._saldo = saldo
    self._taxa_juros = taxa_juros

  @abstractmethod
  def depositar(self, valor):
    pass

  @abstractmethod
  def sacar(self, valor):
    pass

  @abstractmethod
  def calcular_juros(self):
    pass

class ContaCorrente(ContaBancaria):
  """
  Classe para representar uma conta corrente.
  Herda da classe ContaBancaria.
  """

  def depositar(self, valor):
    if valor > 0:
      self._saldo += valor
      print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
      print("Valor de depósito inválido. Deve ser maior que zero.")

  def sacar(self, valor):
    if valor > 0 and valor <= self._saldo:
      self._saldo -= valor
      print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
      print("Valor de saque inválido. Deve ser maior que zero e menor ou igual ao saldo.")

  def calcular_juros(self):
    # Simulação simples de juros mensais
    juros_mensal = self._saldo * (self._taxa_juros / 100) / 12
    self._saldo += juros_mensal
    return juros_mensal

class ContaPoupanca(ContaBancaria):
  """
  Classe para representar uma conta poupança.
  Herda da classe ContaBancaria.
  """

  def depositar(self, valor):
    if valor > 0:
      self._saldo += valor
      print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
      print("Valor de depósito inválido. Deve ser maior que zero.")

  def sacar(self, valor):
    if valor > 0 and valor <= self._saldo:
      self._saldo -= valor
      print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
      print("Valor de saque inválido. Deve ser maior que zero e menor ou igual ao saldo.")

  def calcular_juros(self):
    # Simulação simples de juros anuais
    juros_anual = self._saldo * (self._taxa_juros / 100)
    self._saldo += juros_anual
    return juros_anual

class ContaInvestimento(ContaBancaria):
  """
  Classe para representar uma conta investimento.
  Herda da classe ContaBancaria.
  """

  def depositar(self, valor):
    if valor > 0:
      self._saldo += valor
      print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
      print("Valor de depósito inválido. Deve ser maior que zero.")

  def sacar(self, valor):
    # Simulação de regra específica para saque em conta investimento
    if valor > 0 and valor <= self._saldo * 0.9:  # Limite de saque de 90%
      self._saldo -= valor
      print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
      print("Valor de saque inválido. Deve ser maior que zero e menor ou igual a 90% do saldo.")

  def calcular_juros(self):
    # Simulação de rendimento de investimento (a ser aprimorada de acordo com o tipo de investimento)
    rendimento = self._saldo * 0.02  # Simulando 