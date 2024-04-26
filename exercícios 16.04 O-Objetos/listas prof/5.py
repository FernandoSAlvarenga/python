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
      print(f"Saque de R${valor:.2f} realizado com sucesso na conta de {self.titular}!")
    else:
      print(f"Saldo insuficiente para saque. Saldo disponível: R${self.saldo:.2f}")

  def consultar_saldo(self):
    print(f"Saldo da conta de {self.titular}: R${self.saldo:.2f}")

class ContaPoupanca(Conta):
  
  def __init__(self, titular, saldo, taxa_juros):
    super().__init__(titular, saldo)  # Inicializa a classe base
    self.taxa_juros = taxa_juros

  def render_juros(self):
    juros = self.saldo * (self.taxa_juros / 100)
    self.saldo += juros
    print(f"R${juros:.2f} em juros creditados na conta poupança de {self.titular}!")

class ContaCorrente(Conta):
  

  def __init__(self, titular, saldo, limite_cheque_especial):
    super().__init__(titular, saldo)  # Inicializa a classe base
    self.limite_cheque_especial = limite_cheque_especial

  def sacar(self, valor):
    if valor > 0:
      if valor <= self.saldo:
        # Saque normal com saldo disponível
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso na conta de {self.titular}!")
      else:
        # Saldo insuficiente, usar cheque especial se disponível
        disponivel_cheque_especial = self.limite_cheque_especial - (self.saldo - valor)
        if disponivel_cheque_especial >= 0:
          self.saldo -= valor
          self.limite_cheque_especial -= disponivel_cheque_especial
          print(f"Saque de R${valor:.2f} realizado utilizando o cheque especial da conta de {self.titular}!")
        else:
          print("Saldo insuficiente e limite do cheque especial indisponível.")

# Criação de contas de exemplo
conta_poupanca = ContaPoupanca("Ana Silva", 1000, 10)
conta_corrente = ContaCorrente("João Oliveira", 500, 200)

# Operações nas contas
conta_poupanca.depositar(200)
conta_poupanca.sacar(50)
conta_poupanca.consultar_saldo()
conta_poupanca.render_juros()  # Demonstra o método específico da ContaPoupança

conta_corrente.depositar(350)
conta_corrente.sacar(800)  # Usa cheque especial
conta_corrente.consultar_saldo()