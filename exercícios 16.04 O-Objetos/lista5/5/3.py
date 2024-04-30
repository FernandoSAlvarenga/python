from abc import ABC, abstractmethod

class Veiculo(ABC):
  

  def __init__(self, marca, modelo, ano, cor):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.cor = cor

  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

  @abstractmethod
  def acelerar(self):
    pass

  @abstractmethod
  def frear(self):
    pass


class Carro(Veiculo):
 

  def __init__(self, marca, modelo, ano, cor, tipo_cambio):
    super().__init__(marca, modelo, ano, cor)
    self.tipo_cambio = tipo_cambio

  def ligar(self):
    print(f"Ligando o {self.marca} {self.modelo}...")
    if self.tipo_cambio == "manual":
      print("Pise na embreagem e acione a chave.")
    else:
      print("Acione o botão start.")

  def desligar(self):
    print(f"Desligando o {self.marca} {self.modelo}...")
    print("Verifique se todos os vidros e portas estão fechados.")

  def acelerar(self):
    print(f"Acelerando o {self.marca} {self.modelo}...")
    print("Pise no pedal do acelerador.")

  def frear(self):
    print(f"Freando o {self.marca} {self.modelo}...")
    print("Pise no pedal do freio.")


class Moto(Veiculo):
 

  def __init__(self, marca, modelo, ano, cor, cilindrada):
    super().__init__(marca, modelo, ano, cor)
    self.cilindrada = cilindrada

  def ligar(self):
    print(f"Ligando a {self.marca} {self.modelo}...")
    print("Gire a chave no sentido horário.")

  def desligar(self):
    print(f"Desligando a {self.marca} {self.modelo}...")
    print("Gire a chave no sentido anti-horário.")

  def acelerar(self):
    print(f"Acelerando a {self.marca} {self.modelo}...")
    print("Gire o punho do acelerador.")

  def frear(self):
    print(f"Freando a {self.marca} {self.modelo}...")
    print("Aperte os freios dianteiro e traseiro.")


class Caminhao(Veiculo):
 

  def __init__(self, marca, modelo, ano, cor, capacidade_carga):
    super().__init__(marca, modelo, ano, cor)
    self.capacidade_carga = capacidade_carga

  def ligar(self):
    print(f"Ligando o {self.marca} {self.modelo}...")
    print("Insira a chave na ignição e gire-a.")

  def desligar(self):
    print(f"Desligando o {self.marca} {self.modelo}...")
    print("Gire a chave na ignição e retire-a.")

  def acelerar(self):
    print(f"Acelerando o {self.marca} {self.modelo}...")
    print("Pise no pedal do acelerador.")

  def frear(self):
    print(f"Freando o {self.marca} {self.modelo}...")
    print("Pise no pedal do freio e utilize o freio retardador, se disponível.")

carro1 = Carro("Fiat", "Palio", 2020, "Branco", "manual")
moto1 = Moto("Honda", "CG 160", 2023, "Vermelha", 160)
caminhao1 = Caminhao("Volvo", "FH", 2022, "Azul", 10)

carro1.ligar()
carro1.acelerar()
carro1.frear()
carro1.desligar()

moto1.ligar()