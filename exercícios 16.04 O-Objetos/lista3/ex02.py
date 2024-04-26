'''2: Figuras Geométricas 
Crie as classes: 
Forma (classe base com método calcular_area() abstrato). 
Quadrado (herda de Forma, implementa calcular_area()). 
Retângulo (herda de Forma, implementa calcular_area()). 
Círculo (herda de Forma, implementa calcular_area()). 
Crie uma lista de formas: 
Inclua objetos de Quadrado, Retângulo e Círculo. 
Calcule e mostre: 
A área de cada forma'''

from abc import ABC, abstractmethod

class Forma(ABC):
    
    @abstractmethod
    def calcular_area(self):
        pass
    
    #def descrever(self):
     #   print(f'teste')
    
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
    def __init__(self, diametro):
        self.diametro = diametro 
    
    def calcular_area(self):
        return 3.1415 * self.diametro 

    
areas_figuras = [Quadrado(5), Retangulo(3,4), Circulo(10)]

for forma in areas_figuras:
  print(f"{forma.__class__.__name__} com área: {forma.calcular_area():.2f}")