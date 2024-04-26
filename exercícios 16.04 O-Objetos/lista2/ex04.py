'''
4. Classe Veículo e Carro: 
Crie uma classe abstrata Veiculo com os atributos marca, modelo e ano. 
Crie uma classe Carro que herde de Veiculo. 
Adicione à classe Carro os atributos cor, numero_portas e tipo_cambio. 
Implemente 
métodos ligar(), desligar(), acelerar(), frear() e descrever() nas 
classes Veiculo e Carro. 
Crie um objeto carro1 e chame os métodos adequados.'''

from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frear(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    def descrever(self):
        
        print(f'Modelo: {self.modelo}')
        print(f'Marca: {self.marca}')
        print(f'Ano: {self.ano}')
        
class Carro(Veiculo):
    
    def __init__(self, marca, modelo, ano, cor, num_portas, tipo_cambio):
        super().__init__(marca, modelo, ano)
        self.cor = cor
        self.num_portas = num_portas
        self.tipo_cambio = tipo_cambio
        
    def ligar(self):
        print(f'O {self.modelo} de ano {self.ano} está ligado.')
        
    def acelerar(self):
        print(f"Acelerando o {self.modelo} da montadora {self.marca}")
        
    def frear(self):
        print(f"Velocidade reduzida do {self.modelo} da montadora {self.marca} até a parada total.")

    def desligar(self):
        print(f"Desligando o {self.modelo} da montadora {self.marca}")
        
    def descrever(self):
        super().descrever()
        print(f"A cor do {self.modelo} é {self.cor}")
        print(f"O número de portas do {self.modelo} é {self.num_portas}")
        print(f"O tipo de câmbio do {self.modelo} é {self.tipo_cambio}")
        
carro1 = Carro('Ford', 'Ka', 2019, 'Preto', 4, 'Manual')

print('\n Carro 1: ')

carro1.descrever()
carro1.ligar()
carro1.acelerar()
carro1.frear()
carro1.desligar()
