
class Animal:
 

  def comer(self):
    print(f"{self.__class__.__name__} está comendo...")

  def dormir(self):
    print(f"{self.__class__.__name__} está dormindo...")

class Cachorro(Animal):
 

  def latir(self):
    print(f"{self.__class__.__name__} está latindo: Au au!")

class Gato(Animal):
 

  def miar(self):
    print(f"{self.__class__.__name__} está miando: Miau miau!")

class Papagaio(Animal):
 

  def falar(self):
    print(f"{self.__class__.__name__} está falando: Olá!")

# Criação da lista de animais
animais_do_zoo = [Cachorro(), Gato(), Papagaio()]

# Fazendo os animais comerem, dormirem e realizarem ações específicas
for animal in animais_do_zoo:
  animal.comer()
  animal.dormir()

  if isinstance(animal, Cachorro):
    animal.latir()
  elif isinstance(animal, Gato):
    animal.miar()
  elif isinstance(animal, Papagaio):
    animal.falar()