'''1: Animais no Zoológico 
Crie as classes: 
Animal (classe base com métodos comer() e dormir()). 
Cachorro (herda de Animal, com método latir()). 
Gato (herda de Animal, com método miar()). 
Papagaio (herda de Animal, com método falar()). 
Crie uma lista de animais: 
Inclua objetos de Cachorro, Gato e Papagaio. 
Faça os animais: 
Comerem. 
Dormirem. 
Realizarem ações específicas (latir, miar, falar) de acordo com seu tipo.'''

class Animais:
    # def __init__(self, comer, dormir):
    #     self.comer = comer
    #     self.dormir = dormir

    def dormir(self):
        print(f'{self.__class__.__name__} esta dormindo') # {self.__class__.__name__} pega o nome da classe e passa por parametro.
        
    def comer(self):
        print(f'{self.__class__.__name__} esta se alimentando')


class Cachorro(Animais):
    

    def latir(self):
        print(f'{self.__class__.__name__} esta latindo.')

    
class Gato(Animais):
 

  def miar(self):
    print(f"{self.__class__.__name__} está miando: Miau miau!")

class Papagaio(Animais):
  def falar(self):
    print(f"{self.__class__.__name__} está falando: Olá!")
   
animais_do_zoo = [Cachorro(), Gato(), Papagaio()]

for animal in animais_do_zoo:
  animal.comer()
  animal.dormir()

  if isinstance(animal, Cachorro):
    animal.latir()
  elif isinstance(animal, Gato):
    animal.miar()
  elif isinstance(animal, Papagaio):
    animal.falar()



        
