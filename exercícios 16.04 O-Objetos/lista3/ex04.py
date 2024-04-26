'''Jogo de Cartas 
Crie as classes: 
Carta (classe base com atributos valor e naipe). 
CartaBaralho (herda de Carta, implementa métodos __str__() e comparar()). 
Baralho (armazena cartas, possui métodos para embaralhar, distribuir e 
mostrar cartas). 
Crie um baralho: 
Inclua cartas de diferentes valores e naipes. 
Embaralhe e distribua: 
Distribua cartas para jogadores (por exemplo, 2 cartas para cada um). 
Compare as cartas: 
Utilize o método comparar() para comparar as cartas de dois jogadores.'''

class Carta:
    def __init__(self, valor, naipe):
        self.naipe = naipe
        self.valor = valor

    
    
class Cartabaralho(Carta):
    def __init__(self, valor, naipe):
        super().__init__(valor, naipe)
        
        