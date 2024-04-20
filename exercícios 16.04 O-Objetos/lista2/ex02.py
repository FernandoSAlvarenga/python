'''  2. Classe Figura Geométrica e Círculo: 
Crie uma classe abstrata FiguraGeometrica com os 
métodos calcular_area() e descrever(). 
Crie uma classe Circulo que herde de FiguraGeometrica. 
Implemente o método calcular_area() na classe Circulo para calcular a 
área do círculo. 
Crie um objeto circulo1 e chame os 
métodos calcular_area() e descrever().'''


class Figura_Geometrica:
    def calcular_area(self):#Este método é abstrato (utiliza NotImplementedError), o que significa que ele não possui uma 
        raise NotImplementedError #implementação concreta na classe base. As classes derivadas (Quadrado, Triangulo, Circulo) 
    # serão responsáveis por implementar este método de acordo com a fórmula específica para calcular a área de cada figura_ geométrica.
    def descrever(self):
        raise NotImplementedError
    
class Circulo(Figura_Geometrica):
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
        return 3.1415 * (self.raio * self.raio)
    
circulo1 = Circulo(5)

print(f'Área do circulo é: {circulo1.calcular_area()}')