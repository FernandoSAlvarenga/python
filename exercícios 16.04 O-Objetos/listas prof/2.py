from abc import abstractmethod

class Forma:
 

  @abstractmethod
  def calcular_area(self):
    pass

class Quadrado(Forma):
 

  def __init__(self, lado):
    self.lado = lado

  def calcular_area(self):
    return self.lado * self.lado

class Retangulo(Forma):
 

  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    return self.base * self.altura

class Circulo(Forma):
 
  def __init__(self, raio):
    self.raio = raio

  def calcular_area(self):
    return 3.1415 * self.raio * self.raio

# Criação da lista de formas
formas = [Quadrado(5), Retangulo(7, 4), Circulo(3)]

# Cálculo e exibição da área de cada forma
for forma in formas:
  print(f"{forma.__class__.__name__} com área: {forma.calcular_area():.2f}")