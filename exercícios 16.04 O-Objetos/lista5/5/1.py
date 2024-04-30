from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
 

  def __init__(self, base, altura):
    if base <= 0 or altura <= 0:
      raise ValueError("Base e altura devem ser maiores que zero.")
    self._base = base
    self._altura = altura

  @abstractmethod
  def calcular_area(self):
    pass

class Quadrado(FiguraGeometrica):


  def calcular_area(self):
    return self._base * self._base

class Retangulo(FiguraGeometrica):


  def calcular_area(self):
    return self._base * self._altura

class Triangulo(FiguraGeometrica):


  def calcular_area(self):
    return (self._base * self._altura) / 2

# Exemplo de uso (polimorfismo)
figuras = [Quadrado(5,2), Retangulo(3, 4), Triangulo(6, 8)]  # Polimorfismo

for figura in figuras:
  print(f"{figura.__class__.__name__}: Área = {figura.calcular_area():.2f}")